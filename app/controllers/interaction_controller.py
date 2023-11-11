from fastapi import APIRouter
from database import Database
from schemas import InteractionCreate, InteractionFetch

router = APIRouter()
database = Database()


@router.get("/interactions", response_model=list[InteractionFetch])
def get_interactions():
    interactions = database.get_interactions()
    return interactions


@router.post("/interactions", response_model=InteractionFetch, status_code=201)
def create_interaction(interaction_data: InteractionCreate):
    interaction = database.create_interaction(interaction_data)
    return interaction
