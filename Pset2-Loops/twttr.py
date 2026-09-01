inp = input("Input: ")

for l in inp:
    if l.lower() not in "aeiou":
        print(l, end="")