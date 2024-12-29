import logging
import os

LOG_DIR = 'logs'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


def get_logger(name: str) -> logging.Logger:
    """return a logger with the given name"""
    logger = logging.getLogger(name)
    level = getattr(logging, LOG_LEVEL)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create file handler
    os.makedirs(LOG_DIR, exist_ok=True)
    file_handler = logging.FileHandler(f'{LOG_DIR}/{name}.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
