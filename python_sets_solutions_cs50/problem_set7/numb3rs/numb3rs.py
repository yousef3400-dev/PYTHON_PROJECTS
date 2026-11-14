import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    octet = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    t = re.findall(rf'\b(?:{octet}\.){{3}}{octet}\b',ip)
    if len(t) == 0:
        return False
    else :
        return True




if __name__ == "__main__":
    main()
