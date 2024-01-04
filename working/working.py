import re


def main():
    print(convert(input("Hours: ")))

#two possible formats of input to convert()
#9:00 AM to 5:00 PM
#9 AM to 5 PM

def convert(s):
    #check if user input is in the correct format
    match_obj = re.search(r'^(\d{1,2}(?::\d{2})? (?:AM|PM)) to (\d{1,2}(?::\d{2})? (?:AM|PM))$', s)
    #if input is in correct format, a match object is returned
    if match_obj:
        return check_time(match_obj.group(1))+' '+'to'+' '+check_time(match_obj.group(2))
    else:
        raise ValueError

def check_time(t):
    #extract the hour, min and mediriem part
    if ':' in t:
        #starting here t will be the hour part
        t, min = t.split(':')
        min, meridiem = min.split(' ')
    else:
        t, meridiem = t.split(' ')
        #if exact time then assign to min 00
        min = '00'

    #validate values
    #if hour or min is float str or non-int str then leads to ValueError
    t = int(t)
    min = int(min)
    #check range and meridiem
    if not(meridiem == 'AM' or meridiem == 'PM'):
        raise ValueError
    elif not (t >= 1 and t <=12):
        raise ValueError
    elif not (min >= 0 and min < 60):
        raise ValueError

    #convert values
    if meridiem == 'AM':
        if t == 12:
            t = '00'
        else:
            if t >= 1 and t <= 9:
                t = f'0{t}'
            else:
                t = str(t)
    else:
        if t != 12:
            t = t+12
        t = str(t)
    if min == 0:
        min = '00'
    else:
        if min > 0 and min <= 9:
            min = f'0{min}'
        else:
            min = str(min)
    return t+':'+min

if __name__ == "__main__":
    main()
