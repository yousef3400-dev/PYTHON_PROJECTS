import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    print(convert(sys.argv[1]))


def convert(args):
    try:
        l = []

        with open(args) as file:
            reader = csv.reader(file)
            for row in reader :
                l.append(row)
            return(tabulate(l[1:],headers = l[0], tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
