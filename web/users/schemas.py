from pydantic import BaseModel, ConfigDict
from datetime import datetime


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


class UpdateStreakSchema(BaseModel):
    submit_time: datetime
