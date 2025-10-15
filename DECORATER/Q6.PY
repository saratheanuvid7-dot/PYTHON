def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func()
    return wrapper

@count_calls
def greet():
    print("Hello!")

greet()
greet()
greet()
