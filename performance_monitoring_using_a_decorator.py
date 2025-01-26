import time

def capture_execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.6f}s")
    return wrapper

@capture_execution_time
def our_function():
    time.sleep(3)

@capture_execution_time
def our_other_function():
    time.sleep(5)

our_function()

our_other_function()
