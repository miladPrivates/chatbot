from fastapi import APIRouter, HTTPException

from ai import generate_response
from database import Database
from schemas import MessageCreate, MessageFetch

router = APIRouter()
database = Database()

@router.get("/interactions/{interaction_id}/messages", response_model=list[MessageFetch])
def get_messages(interaction_id: str):
    messages = database.get_messages(interaction_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Messages not found")
    return messages


@router.post("/interactions/{interaction_id}/messages", response_model=MessageFetch, status_code=201)
def create_message(interaction_id: str, message_data: MessageCreate):
    interaction = database.get_interaction(interaction_id)
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    if "messages" in interaction:
        extracted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in interaction["messages"]]
    else:
        extracted_messages = []
    extracted_messages.append(dict(message_data))
    new_ai_generated_response = MessageCreate(role="ai",content=generate_response(extracted_messages))
    database.create_message(interaction_id, message_data)
    ai_message = database.create_message(interaction_id, new_ai_generated_response)
    return ai_message
