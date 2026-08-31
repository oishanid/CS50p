camel = input("camelCase: ")

for l in camel:
    if l.isupper():
        camel = camel.replace(l, "_" + l.lower())