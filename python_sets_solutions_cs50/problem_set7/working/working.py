import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)"
    match = re.fullmatch(pattern, s)
    if not match:
        raise ValueError("invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()
    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if not 1 <= hour <= 12 or not 0 <= minute <= 59:
        raise ValueError("invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    elif hour != 12:
        hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
