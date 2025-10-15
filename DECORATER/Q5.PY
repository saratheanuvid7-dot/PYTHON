def make_uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@make_uppercase
def message():
    return "hello python decorator"

print(message())
