import validators


def main():
    email = input("What's your email address? ")
    print(is_valid(email))


def is_valid(email):
    if validators.email(email):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
