groceries = {}

while True:
    try:
        grocery = input().upper()
        if grocery in groceries:
            groceries[grocery] += 1
        else:
            groceries[grocery] = 1
    except EOFError:
        break

for grocery in sorted(groceries):
    print(f"{groceries[grocery]} {grocery}")
