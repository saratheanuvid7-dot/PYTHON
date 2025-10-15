try:
    print("Trying...")
except ValueError:
       print("Caught ValueError")
else:
       print("No exception occurred")
finally:
       print("Finally done")
