import sys


def main():
    lines = read_lines(get_file())
    print(lines)


def get_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        file = sys.argv[1]
        if not file.endswith(".py"):
            sys.exit("Not a Python file")
        return file


def read_lines(filename):
    lines = 0
    try:
        with open(filename) as file:
            for line in file:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                lines += 1
    except FileNotFoundError:
        sys.exit("Not a Python file")
    return lines


if __name__ == "__main__":
    main()