def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1

for i in infinite_counter():
    if i > 5:
        break
    print(i)
