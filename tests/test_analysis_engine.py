import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.ai.analysis import AnalysisEngine
from app.ai.llm import LLMResponse
from app.ai.result import (
    AnalysisResult,
    ArchitectureResult,
    ProjectContext,
    ProjectFile,
    ProjectFiles,
    RecommendationResult,
    RoadmapResult,
)
from app.models.enums import (
    RecommendationCategory,
    RecommendationComponent,
    RecommendationPriority,
)


class DummyContextBuilder:
    def build(self, project):
        return ProjectContext(project_name=project.project_name, content="context")


class DummyPromptBuilder:
    def build(self, context, schema=None):
        return f"{context.project_name}:{schema or 'default'}"


class DummyLLM:
    def generate(self, prompt):
        return LLMResponse(text='{"summary":"ok","architecture":{"diagram_data":{},"layers":[],"dependencies":[]},"documentation":"doc","roadmap":{"roadmap_data":{}},"recommendation":{"title":"t","description":"d","component":"Architecture","priority":"Medium","category":"Best Practice"}}')


class DummyParser:
    def parse(self, response):
        return AnalysisResult(
            summary="ok",
            architecture=ArchitectureResult(),
            documentation="doc",
            roadmap=RoadmapResult(),
            recommendation=RecommendationResult(
                title="t",
                description="d",
                component=RecommendationComponent.ARCHITECTURE,
                priority=RecommendationPriority.MEDIUM,
                category=RecommendationCategory.BEST_PRACTICE,
            ),
        )


def test_analysis_engine_builds_prompt_and_returns_result():
    project = ProjectFiles(
        project_name="demo",
        root_path="/tmp/demo",
        files=[ProjectFile(path="app.py", content="print('hi')")],
    )

    engine = AnalysisEngine(
        context_builder=DummyContextBuilder(),
        prompt_builder=DummyPromptBuilder(),
        llm=DummyLLM(),
        parser=DummyParser(),
    )

    result = engine.analyze_project(project)

    assert result.summary == "ok"
    assert result.documentation == "doc"
