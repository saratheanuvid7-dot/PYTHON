def squares(n):
    for i in range(1, n + 1):
        yield i * i

for sq in squares(5):
    print(sq)
