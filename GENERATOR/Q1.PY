def number_gen():
    for i in range(1, 6):
        yield i

for num in number_gen():
    print(num)
