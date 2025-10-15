def odd_numbers(limit):
    for i in range(1, limit+1, 2):
        yield i

print(list(odd_numbers(10)))
