import sys
import csv

def main():
    check_arg()
    file_process()

def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

def file_process():
    try:
        with open(sys.argv[1]) as before:
            students = []
            csv_reader = csv.reader(before)
            next(csv_reader)
            for row in csv_reader:
                last, first = row[0].replace(' ','').split(',')
                students.append({'first':first, 'last':last, 'house':row[1]})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    with open(sys.argv[2],'w') as after:
        csv_writer = csv.DictWriter(after, fieldnames = ['first', 'last', 'house'])
        csv_writer.writeheader()
        for student in students:
            csv_writer.writerow(student)

if __name__ == '__main__':
    main()

