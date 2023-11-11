import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.handlers.RotatingFileHandler(
                filename=os.path.join(logs_dir, "chatbots.log"),
                maxBytes=1024 * 1024,  # 1MB
                backupCount=100
            )
        ]
    )
