from pydantic import BaseModel, ConfigDict
from datetime import datetime


class EventSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    emotional_state: str
    data: dict
    created_at: datetime
    updated_at: datetime
