def repeat_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat_twice
def greet():
    print("Hi there!")

greet()
