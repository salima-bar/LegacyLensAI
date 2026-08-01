from enum import Enum
from typing import Any, NamedTuple, get_args, get_origin

from pydantic import BaseModel
from pydantic.fields import FieldInfo


class TypeInfo(NamedTuple):
    """
    Information extracted from a Python type annotation.
    """

    display_name: str

    inner_type: Any | None = None

    is_model: bool = False

    is_enum: bool = False

    is_list: bool = False

    is_optional: bool = False

    is_dict: bool = False


class SchemaBuilder:
    """
    Builds an LLM-friendly schema description from Pydantic models.
    """

    def __init__(self) -> None:
        self._lines: list[str] = []
        self._visited_models: set[type[BaseModel]] = set()

    def build_schema(
        self,
        model: type[BaseModel],
    ) -> str:
        """
        Build the complete schema for a Pydantic model.
        """

        self._lines.clear()
        self._visited_models.clear()
        self._build_model(
            model=model,
            level=0,
        )

        return "\n".join(self._lines)

    def _build_model(
        self,
        model: type[BaseModel],
        level: int,
    ) -> None:
        """
        Build a Pydantic model and all of its fields.
        """

        # Prevent infinite recusion.
        if model in self._visited_models:  
            return

        self._visited_models.add(model)

        # Model name.
        self._lines.append(
            self._indent(level) + model.__name__
        )

        # Model description (if available).
        if model.__doc__:

            description = model.__doc__.strip()

            if description:

                self._lines.append(
                    self._indent(level + 1) + description
                )

        # Empty line before fields.
        self._lines.append("")

        # Build model fields.
        self._build_fields(
            model=model,
            level=level + 1,
        )

    def _build_fields(
        self,
        model: type[BaseModel],
        level: int,
    ) -> None:
        """
        Build every field of a model.
        """

        for field_name, field in model.model_fields.items():

            self._build_field(
                field_name=field_name,
                field=field,
                level=level,
            )

    def _build_field(
        self,
        field_name: str,
        field: FieldInfo,
        level: int,
    ) -> None:
        """
        Build a single model field.
        """

        annotation = field.annotation

        constraints = self._build_constraints(field)

        type_info = self._format_type(
            annotation,
        )

        self._lines.append(
            self._indent(level)
            + f"{field_name} ({type_info.display_name})"
        )

        if field.description:

            self._lines.append(
                self._indent(level + 1)
                + field.description
            )

        if constraints:

            self._lines.append("")

            for constraint in constraints:

                self._lines.append(
                        self._indent(level + 1)
                        + constraint
                )
        llm_hint = None

        if field.json_schema_extra:

            llm_hint = field.json_schema_extra.get(
                "llm_hint"
            )

        if llm_hint:

            self._lines.append("")

            self._lines.append(
                self._indent(level + 1)
                + "LLM Hint:"
            )

            self._lines.append(
                self._indent(level + 2)
                + llm_hint
            )

            self._lines.append("")

        if type_info.is_enum:

            self._build_enum(
                enum_type=type_info.inner_type,
                level=level + 1,
            )


        if type_info.is_model:

            self._build_model(
                model=type_info.inner_type,
                level=level + 1,
            )

    def _build_constraints(self, field: FieldInfo) -> list[str]:
        """
        Extract human-readable validation constraints
        from a Pydantic field.
        """
        constraints: list[str] = []
    
    
        # String constraints
        if hasattr(field, 'min_length') and field.min_length is not None:
            constraints.append(f"Minimum length: {field.min_length} characters.")
    
        if hasattr(field, 'max_length') and field.max_length is not None:
            constraints.append(f"Maximum length: {field.max_length} characters.")
    
        if hasattr(field, 'pattern') and field.pattern is not None:
            constraints.append(f"Must match pattern: {field.pattern}")
    
        # Numeric constraints
        if hasattr(field, 'ge') and field.ge is not None:
            constraints.append(f"Minimum value: {field.ge}")
    
        if hasattr(field, 'gt') and field.gt is not None:
            constraints.append(f"Value must be greater than {field.gt}")
    
        if hasattr(field, 'le') and field.le is not None:
            constraints.append(f"Maximum value: {field.le}")
    
        if hasattr(field, 'lt') and field.lt is not None:
            constraints.append(f"Value must be less than {field.lt}")
    
        return constraints
    
    def _indent(
        self,
        level: int,
    ) -> str:
        """
        Return indentation spaces.
        """

        return "    " * level

    def _format_type(
        self,
        annotation: Any,
    ) -> TypeInfo:
       """
        Convert a Python annotation into
        an LLM-friendly type.
        """
       if self._is_optional(annotation):
            return self._format_optional_type(annotation)

       origin = get_origin(annotation)

       if origin is list:
            return self._format_list_type(annotation)

       if origin is dict:
            return self._format_dict_type(annotation)

       if self._is_pydantic_model(annotation):
            return self._format_model_type(annotation)

       if self._is_enum(annotation):
            return TypeInfo(
                display_name="Enum",
                inner_type=annotation,
                is_enum=True,
            )

       return self._format_builtin_type(annotation)

    def _format_builtin_type(
        self,
        annotation: Any,
    ) -> TypeInfo:
        """
        Format Python built-in types.
        """

        mapping = {
            str: "String",
            int: "Integer",
            float: "Number",
            bool: "Boolean",
        }

        return TypeInfo(
            display_name=mapping.get(
                annotation,
                "Unknown",
            )
        )


    def _format_list_type(
        self,
        annotation: Any,
    ) -> TypeInfo:
        """
        Format list types.
        """

        inner_type = self._extract_inner_type(annotation)

        if self._is_pydantic_model(inner_type):

            return TypeInfo(
                display_name="List of objects",
                inner_type=inner_type,
                is_model=True,
                is_list=True,
            )

        if self._is_enum(inner_type):

            return TypeInfo(
                display_name="List of enums",
                inner_type=inner_type,
                is_enum=True,
                is_list=True,
            )

        builtin = self._format_builtin_type(inner_type)

        mapping = {
                "String": "List of strings",
                "Integer": "List of integers",
                "Number": "List of numbers",
                "Boolean": "List of booleans",
            }
        return TypeInfo(
            display_name=mapping.get(
                builtin.display_name,
                "List",
            ),
            inner_type=inner_type,
            is_list=True,
            )


    def _format_dict_type(
        self,
        annotation: Any,
    ) -> TypeInfo:
        """
        Format dictionary types.
        """

        return TypeInfo(
            display_name="Structured object",
            is_dict=True,
        )


    def _format_model_type(
        self,
        annotation: type[BaseModel],
    ) -> TypeInfo:
        """
        Format nested Pydantic models.
        """

        return TypeInfo(
            display_name="Object",
            inner_type=annotation,
            is_model=True,
        )

    def _format_optional_type(
        self,
        annotation: Any,
    ) -> TypeInfo:
        """
        Format optional types.
        """

        inner_type = self._extract_inner_type(annotation)

        info = self._format_type(inner_type)

        return TypeInfo(
            display_name=f"{info.display_name} or null",
            inner_type=info.inner_type,
            is_model=info.is_model,
            is_enum=info.is_enum,
            is_list=info.is_list,
            is_optional=True,
            is_dict=info.is_dict,
        )

    def _extract_inner_type(
        self,
        annotation: Any,
    ) -> Any:
        """
        Extract the first inner type from generic annotations.
        """

        args = get_args(annotation)

        if not args:
            return annotation

        return args[0]

    def _is_pydantic_model(
        self,
        annotation: Any,
    ) -> bool:
        """
        Return True if the annotation is a Pydantic model.
        """

        return (
            isinstance(annotation, type)
            and issubclass(annotation, BaseModel)
        )


    def _is_enum(
        self,
        annotation: Any,
    ) -> bool:
        """
        Return True if the annotation is an Enum.
        """

        return (
            isinstance(annotation, type)
            and issubclass(annotation, Enum)
        )


    def _is_optional(
        self,
        annotation: Any,
    ) -> bool:
        """
        Return True if the annotation is Optional.
        """

        origin = get_origin(annotation)

        if origin is None:
            return False

        return type(None) in get_args(annotation)


    def _build_enum(
        self,
        enum_type: type[Enum],
        level: int,
    ) -> None:
        """
        Build all enum values.
        """

        self._lines.append(
            self._indent(level)
            + "Allowed values:"
        )

        for member in enum_type:

            self._lines.append(
                self._indent(level + 1)
                + f"- {member.value}"
            )

        self._lines.append("")


def build_schema(
    model: type[BaseModel],
) -> str:
    """
    Convenience function.
    """

    return SchemaBuilder().build_schema(model)