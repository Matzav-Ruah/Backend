from datetime import datetime
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict

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
    last_name: Optional[str]
    streak_count: int
    settings: dict
    created_at: datetime
    updated_at: datetime
    in_leaderboard: bool


class UserProfileSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: Optional[str]
    streak_count: int


class StreakSchema(BaseModel):
    streak_count: int


class UpdateNameSchema(BaseModel):
    first_name: str
    last_name: str


class ShowInLeaderboardSchema(BaseModel):
    in_leaderboard: bool
