def table(n):
    for i in range(1, 11):
        yield n * i

for val in table(3):
    print(val)
