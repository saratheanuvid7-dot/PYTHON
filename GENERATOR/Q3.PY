def table(n):
    for i in range(1, 11):
        yield n * i

for val in table(5):
    print(val)
