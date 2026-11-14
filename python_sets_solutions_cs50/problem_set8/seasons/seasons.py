import re
import sys
from datetime import date

import inflect

p = inflect.engine()


def main():
    try:
        s = input("Date of Birth: ")
    except EOFError:
        sys.exit("Invalid date")

    birth = parse_date(s)
    if birth is None or birth > date.today():
        sys.exit("Invalid date")

    print(minutes_in_words(birth, date.today()))


def parse_date(s):
    s = s.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def minutes_in_words(birth, today):
    minutes = (today - birth).days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
