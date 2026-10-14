import logging

def configure(level: str = "INFO") -> logging.Logger:
    """Configure and return the gateway's root logger."""
    logger = logging.getLogger("gateway")
    logger.setLevel(level)
    return logger
