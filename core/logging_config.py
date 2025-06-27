import logging
import os
from logging.handlers import RotatingFileHandler

def log_setup():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        "%(levelname)s:     %(message)s"
    ))
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "app.log")

    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=1024 * 1024 * 5,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    ))
    logger.addHandler(file_handler)

    return logging.getLogger("app")