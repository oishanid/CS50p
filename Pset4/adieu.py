import inflect
p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except:
        print()
        break

goodbye = p.join(names, final_sep=",")
print(f"Adieu, adieu, to {goodbye}")
