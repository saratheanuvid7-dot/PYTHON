def infinite_numbers(start=1):
    while True:
        yield start
        start += 1

gen = infinite_numbers()
for i in range(5):
    print(next(gen))
