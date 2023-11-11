import logging
from fastapi import FastAPI
from controllers.routes import router
import utils

app = FastAPI()
app.include_router(router)

logger = logging.getLogger(__name__)


@app.on_event("startup")
def startup_event():
    utils.setup_logging()
    logger.info(f"app started")


@app.on_event("shutdown")
def shutdown_event():
    logger.info(f"app shutting down")
