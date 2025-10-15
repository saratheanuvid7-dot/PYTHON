try:
    print("Before error")
    x = 10 / 0   
    print("This line will NOT run")  # Skipped
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")

print("Program continues after exception handling")
