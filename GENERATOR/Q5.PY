def char_gen(word):
    for ch in word:
        yield ch

for letter in char_gen("Python"):
    print(letter)
