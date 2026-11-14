import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile, outfile = sys.argv[1], sys.argv[2]
    if not infile.endswith(".csv") or not outfile.endswith(".csv"):
        sys.exit("Not a CSV file")

    convert(infile, outfile)


def convert(infile, outfile):
    try:
        with open(infile, "r", newline="") as f_in:
            reader = csv.DictReader(f_in)
            rows = []
            for row in reader:
                last, first = row["name"].split(", ", 1)
                rows.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")

    with open(outfile, "w", newline="") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
