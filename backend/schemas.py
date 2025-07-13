from pydantic import BaseModel
from datetime import date

class TimelineEventBase(BaseModel):
    title: str
    date: date
    description: str
    image_url: str | None = None
    source_url: str | None = None
    tags: str | None = None

class TimelineEventCreate(TimelineEventBase):
    pass

class TimelineEvent(TimelineEventBase):
    id: int

    class Config:
        orm_mode = True
