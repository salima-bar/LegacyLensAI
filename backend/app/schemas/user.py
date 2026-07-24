from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


# ===========================
# Base Schema
# ===========================

class UserBase(BaseModel):
    full_name: str
    email: EmailStr


# ===========================
# Create
# ===========================

class UserCreate(UserBase):
    password: str


# ===========================
# Update
# ===========================

class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


# ===========================
# Read
# ===========================

class UserRead(UserBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)