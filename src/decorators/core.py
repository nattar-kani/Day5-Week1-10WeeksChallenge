from functools import wraps
import logging

logger = logging.getLogger("pyforge")

def log_calls(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        logger.info(
            f"function={func.__name__} | function started"
        )

        try:
            result = func(*args,**kwargs)
        except Exception:
            logger.exception(
                f"function={func.__name__} | function failed"
            )
            raise

        logger.info(
            f"function={func.__name__} | function completed"
        )

        return result
    return wrapper