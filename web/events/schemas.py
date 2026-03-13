from typing import Generic, Literal, Optional, TypeVar
from pydantic import BaseModel, ConfigDict
from datetime import datetime

T = TypeVar("T")

EMOTIONAL_STATE_CHOICES = Literal["bad", "neutral", "good"]


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: T


class EventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    emotional_state: str
    event_data: dict
    date: datetime
    created_at: datetime
    updated_at: datetime


class CreateEventSchema(BaseModel):
    emotional_state: EMOTIONAL_STATE_CHOICES
    data: dict


class UpdateEventSchema(BaseModel):
    emotional_state: Optional[EMOTIONAL_STATE_CHOICES] = None
    data: Optional[dict] = None
