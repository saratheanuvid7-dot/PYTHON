def handle_error(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print("An error occurred:", e)
    return wrapper

@handle_error
def divide_by_zero():
    print(10 / 0)  # This will raise an error

divide_by_zero()
