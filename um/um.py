import re


def main():
    print(count(input("Text: ")))


def count(s):
    #case insensitive so ignore case
    match_obj = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(match_obj)

if __name__ == "__main__":
    main()
