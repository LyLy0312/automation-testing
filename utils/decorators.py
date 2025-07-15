import functools
import time

def screenshot_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        filename = args[1] if len(args) > 1 else kwargs.get("name", "unknown.png")
        try:
            print(f"[Start Screenshot] {filename}")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[Done Screenshot] {filename} in {round(end - start, 2)}s")
            return result
        except Exception as e:
            print(f"[Error Screenshot] {filename} - {str(e)}")
            raise
    return wrapper
