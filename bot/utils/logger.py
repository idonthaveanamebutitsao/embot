import logging
from bot.config import LOG_FORMAT, LOG_LEVEL

def setup_logger(name):
    """
    Creates and returns a logger instance with the specified configuration
    """
    logger = logging.getLogger(name)
    
    # Set the logging level
    logger.setLevel(LOG_LEVEL)
    
    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger
