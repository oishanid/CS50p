import random


def main():
    level = get_level()
    score = 0
    for _ in range(0, 10):
        attempts = 3
        int1, int2 = generate_integer(level), generate_integer(level=level)
        while attempts > -1:
            if attempts == 0:
                print(f"{int1} + {int2} = {int1 + int2}")
                break
            try:
                answer = int(input(f"{int1} + {int2} = "))
                if answer == int1 + int2:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts -= 1
                    pass
            except:
                print("EEE")
                attempts -= 1
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)
    else:
        raise ValueError
    return integer


if __name__ == "__main__":
    main()
