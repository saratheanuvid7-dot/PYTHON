import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished running...")

slow_function()
