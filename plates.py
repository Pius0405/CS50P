def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not(s.isalnum()):
        return False
    if not(s[0:2].isalpha):
        return False
    for index in range(len(s)):
        char = s[index]
        if char.isdigit():
            if int(char) == 0:
                return False
            if not(s[index:len(s)].isdigit()):
                return False
            break
    return True


main()
