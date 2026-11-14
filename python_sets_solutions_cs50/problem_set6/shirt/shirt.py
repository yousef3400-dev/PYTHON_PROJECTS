import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile, outfile = sys.argv[1], sys.argv[2]

    valid = (".jpg", ".jpeg", ".png")
    in_ext = os.path.splitext(infile)[1].lower()
    out_ext = os.path.splitext(outfile)[1].lower()

    if in_ext not in valid or out_ext not in valid:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(infile)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(outfile)


if __name__ == "__main__":
    main()
