amount_due = 50
accepted = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    cents = int(input("Insert Coin: "))
    if cents in accepted:
        amount_due -= cents
    else:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")