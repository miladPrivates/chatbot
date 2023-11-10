from pydantic import BaseModel
from datetime import datetime


class InteractionCreate(BaseModel):
    settings: dict


class InteractionFetch(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    settings: dict
    messages: list[dict]


class MessageCreate(BaseModel):
    role: str
    content: str


class MessageFetch(BaseModel):
    id: str
    created_at: datetime
    role: str
    content: str
