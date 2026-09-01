import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
        else:
            pass
    except:
        pass

integer = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > integer:
            print("Too large!")
        elif 0 < guess < integer:
            print("Too small!")
        elif guess == integer:
            print("Just right!")
            break
        else:
            pass
    except:
        pass
