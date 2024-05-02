from loguru import logger


def debug(func):
    def wrapper():
        logger.info(f"start {func.__name__}")
        func()
        logger.info(f"end {func.__name__}")

    return wrapper
