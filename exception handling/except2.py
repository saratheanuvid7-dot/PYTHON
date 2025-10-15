try:
  result = 1 / 0
except Exception:
       print("Caught general exception")
except ZeroDivisionError:
       print("Caught division error")
