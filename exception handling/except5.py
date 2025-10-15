try:
       1 / 0
except ZeroDivisionError:
       raise ValueError("New error")
finally:
       print("Finally")
     
