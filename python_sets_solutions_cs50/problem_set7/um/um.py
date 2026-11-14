import re


def main():
    text = input("Text: ")
    print(count(text))


def count(s):
    h =re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(h)


if __name__ == "__main__":
    main()
