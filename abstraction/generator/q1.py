def simple_gen():
    yield 10
    yield 20
    yield 30

for value in simple_gen():
    print(value)
