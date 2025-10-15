try:
    try:
        print("Inner try starts")
        x = 10 / 0   # ❌ Exception here
    except ValueError:
        print("Inner except (not matching)")  # Won't run
    print("This line is skipped after error in inner try")
except ZeroDivisionError:
    print("Outer except caught the error!")


