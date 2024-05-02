from loguru import logger


def debug(func):

    def wrapper(*args, **kwargs):
        logger.debug(f"start {func.__name__}")
        logger.debug(f"Args: {args}")
        logger.debug(f"Kwargs: {kwargs}")

        func(*args, **kwargs)
        logger.debug(f"end {func.__name__}")

    return wrapper
