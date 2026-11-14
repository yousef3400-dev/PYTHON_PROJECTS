
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            parts = date.split()

            if len(parts) != 3 or parts[1][-1] != ",":
                continue

            month = months.index(parts[0]) + 1
            day = int(parts[1][:-1])
            year = int(parts[2])

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        pass
