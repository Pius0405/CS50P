import datetime
import sys
import re
import inflect
p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    if not validate_dob(dob):
        sys.exit("Invalid date format")
    mins = get_minutes(dob)
    mins_in_word = get_word(mins)
    print(mins_in_word)

def validate_dob(dob):
    #valid format of dob: YYYY-MM-DD
    #check if dob in valid format
    if match := re.search(r'^\d{4}-\d{2}-\d{2}$', dob):
        return True
    else:
        return False

def get_minutes(dob):
    date_obj = datetime.date.fromisoformat(dob)
    delta_obj = datetime.date.today() - date_obj
    return int(delta_obj.total_seconds()/60)

def get_word(mins):
    return p.number_to_words(mins, andword="").capitalize()+' minutes'

if __name__ == "__main__":
    main()
