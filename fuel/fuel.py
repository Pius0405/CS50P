def main():
    fuel = get_fuel()
    if fuel <= 1:
        print('E')
    elif fuel >= 99:
        print('F')
    else:
        print(str(fuel)+'%')

def get_fuel():
    while True:
        try:
            x,y = input('Fraction: ').split('/')
            x = int(x)
            y = int(y)
            if x <= y:
                percentage = (x/y)*100
                return round(percentage)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


main()





