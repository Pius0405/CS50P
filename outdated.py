months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    year, day, month = get_info()
    new_date = form_date(year, month, day)
    print(new_date)


def get_info():
    while True:
        date = input('Date: ').strip()
        try:
            #checking format 1
            month, day, year = date.split('/')
            if int(month) <= 12 and int(day) <= 31:
                return year, day, month
        except ValueError:
            try:
                #checking format 2
                month, day, year = date.split(' ')
                if ',' in day:
                    day = day.strip(',')
                    if month in months and int(day) <= 31:
                        return year, day, str(months.index(month)+1)
            except ValueError:
                pass

def form_date(y, m, d):
    new_date = f'{int(y)}-{int(m):02}-{int(d):02}'
    return new_date

main()


