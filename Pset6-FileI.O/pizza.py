from tabulate import tabulate
import sys, csv


def main():
    read_csv(get_file())


def get_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        file = sys.argv[1]
        if not file.endswith(".csv"):
            sys.exit("Not a CSV file")
        return file


def read_csv(filename):
    data = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                pizza, small, large = row[0], row[1], row[2]
                data.append([pizza, small, large])
    except FileNotFoundError:
        sys.exit("Not a CSV file")
    print(tabulate(data, tablefmt="grid", headers="firstrow"))


if __name__ == "__main__":
    main()