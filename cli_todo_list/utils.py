from functools import wraps
from typing import Callable

def input_errors(func: callable) -> Callable:
    @wraps
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return 'Not enough arguments.'
        except KeyError:
            return 'Task not found.'
        except AttributeError:
            return 'Operation failed. Task may not exist.'
        except Exception as err:
            return f'Error: {err}'
    return inner