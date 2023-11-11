from fastapi import APIRouter
from controllers import interaction_controller, message_controller

router = APIRouter()

router.include_router(interaction_controller.router)
router.include_router(message_controller.router)
