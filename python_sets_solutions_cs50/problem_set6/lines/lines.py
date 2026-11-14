import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    print(count_lines(filename))


def count_lines(filename):
    count = 0
    try:
        with open(filename) as file:
            for line in file:
                stripped = line.lstrip()
                if stripped == "" or stripped.startswith("#"):
                    continue
                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


if __name__ == "__main__":
    main()
