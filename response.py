from validator_collection import validators, checkers

def main():
    email = input("What's your email address? ")
    if validate_email(email):
        print('Valid')
    else:
        print('Invalid')


def validate_email(e):
    return checkers.is_email(e)

if __name__ == '__main__':
    main()
