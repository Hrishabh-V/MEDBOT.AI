import logging
import os
from datetime import datetime
from src.core.config import LOG_LEVEL

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"medbot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

def setup_logger(name='medbot'):
    logger = logging.getLogger(name)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)
    logger.propagate = False

    # Custom formatter example
    fmt = logging.Formatter(
        '[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(fmt)
    logger.addHandler(console)

    fileh = logging.FileHandler(LOG_FILE, encoding='utf-8')
    fileh.setLevel(level)
    fileh.setFormatter(fmt)
    logger.addHandler(fileh)

    return logger

logger = setup_logger()


