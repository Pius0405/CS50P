import sys
import csv
from tabulate import tabulate

def main():
    filename = check_arg()
    output_table(filename)

def check_arg():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) <2:
        sys.exit('Too few command-line arguments')
    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        return sys.argv[1]

def output_table(f):
    try:
        pizzas = []
        with open(f) as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                pizzas.append(row)
        table = tabulate(pizzas, headers = "keys", tablefmt = "grid")
        print(table)
    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == '__main__':
    main()
