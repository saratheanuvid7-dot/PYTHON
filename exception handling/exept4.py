try:
    print("Step 1: Try block starts")
    x = 10 / 0   # ❌ Exception here
    print("This line in try won't run")
except ZeroDivisionError:
    print("Step 2: Except block runs")
else:
    print("Else block runs (only if no exception)")  # Skipped
finally:
    print("Step 3: Finally block always runs")
