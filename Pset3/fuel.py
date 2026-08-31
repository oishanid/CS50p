while True:
    try:
        fraction = input("Fraction: ")
        x, y = (fraction.split("/"))
        x = int(x)
        y = int(y)
        answer = x/y
        if y == 0 or not isinstance(x, int) or not isinstance(y, int) or x != abs(x) or x>y:
            continue
        else:
            percent = int(round(answer * 100, 0))
            break
    except:
        pass

if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent}%")
