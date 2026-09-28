import sys, csv


def main():
    rows = read_csv(get_file())
    with open(sys.argv[2], "w") as file:
        #  Create and write a cleaned csv (I used the name after.csv)
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for name, house in rows:
            last, first = name.split(", ")
            writer.writerow({"first": first, "last": last, "house": house})


def get_file():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        file = sys.argv[1]
        if not file.endswith(".csv"):
            sys.exit("Not a CSV file")
        return file


def read_csv(filename):
    rows = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append((row["name"], row["house"]))
    except FileNotFoundError:
        sys.exit("Not a CSV file")
    return rows


if __name__ == "__main__":
    main()
