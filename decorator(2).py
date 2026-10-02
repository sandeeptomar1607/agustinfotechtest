

import time
from functools import wraps


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time_taken = end_time - start_time
        print(f"Time taken by the func: {execution_time_taken}")

        return result
    return wrapper

@execution_time
def process_data():
    time.sleep(2)
    return "Data processed successfully"

result = process_data()

print(result)

