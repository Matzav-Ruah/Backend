from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None


class SignInSchema(BaseModel):
    email: str
    password: str


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    settings: dict
    streak_count: int
    created_at: datetime
    updated_at: datetime


class UserProfileSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    streak_count: int


class StreakSchema(BaseModel):
    streak_count: int
