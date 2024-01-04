import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if match := re.search(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip):
        for i in range(1,5):
            num = int(match.group(i))
            if num < 0 or num > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
