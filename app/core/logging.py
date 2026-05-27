import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configure_logging() -> logging.Logger:
    Path("logs").mkdir(exist_ok=True)

    handler = RotatingFileHandler(
        "logs/security.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler],
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    return logging.getLogger("vectolab")
