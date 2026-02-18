from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

EMOTIONAL_STATE_CHOICES = Literal["bad", "neutral", "good"]


class EventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    emotional_state: str
    data: dict
    created_at: datetime
    updated_at: datetime


class CreateEventSchema(BaseModel):
    emotional_state: EMOTIONAL_STATE_CHOICES
    data: dict


class UpdateEventSchema(BaseModel):
    emotional_state: Optional[EMOTIONAL_STATE_CHOICES] = None
    data: Optional[dict] = None
