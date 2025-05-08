# app/core/logger.py
import logging

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
