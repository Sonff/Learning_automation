# =====================================================================
# TASK MANAGER PROJECT: PYDANTIC SCHEMAS (schemas.py)
# =====================================================================
# Request payload aur response structural verification models.

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

# ---------------------------------------------------------------------
# User Schemas
# ---------------------------------------------------------------------
class UserRegisterSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"

# ---------------------------------------------------------------------
# Task Schemas
# ---------------------------------------------------------------------
class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    priority: int = Field(default=3, ge=1, le=5, description="Priority rating from 1 (highest) to 5 (lowest)")

class TaskUpdateSchema(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    status: Optional[TaskStatus] = None

class TaskResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    priority: int
    status: TaskStatus
    owner: str

    class Config:
        # Pydantic validation conversion support
        from_attributes = True
