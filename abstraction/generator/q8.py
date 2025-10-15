def reverse_string(s):
    for char in reversed(s):
        yield char

print(''.join(reverse_string("Python")))
