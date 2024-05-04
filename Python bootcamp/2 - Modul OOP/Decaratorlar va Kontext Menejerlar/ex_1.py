from functools import wraps
from datetime import datetime
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"- called function: {func.__name__} at {start_time.strftime('%H:%M:%S')}")
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"- finished function: {func.__name__} at {end_time.strftime('%H:%M:%S')}")
        return result
    return wrapper
@log
def hello():
    print("hello")

hello()
