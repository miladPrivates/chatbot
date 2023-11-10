from pydantic import BaseModel
from datetime import datetime


class Interaction(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    settings: dict
    messages: list[dict]


class Message(BaseModel):
    id: str
    created_at: datetime
    role: str
    content: str
