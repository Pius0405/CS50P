import sys

def main():
    check_argument()
    loc = count_lines()
    print(loc)


def check_argument():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif not sys.argv[1].endswith('.py'):
        sys.exit('Not a python file')

def count_lines():
    try:
        with open(sys.argv[1]) as file:
            lines = 0
            for line in file:
                if check_line(line):
                    lines += 1
        return lines
    except FileNotFoundError:
        sys.exit('File does not exist')

def check_line(line):
    line = line.lstrip()
    if line.startswith('#') or line == '':
        return False
    else:
        return True

if __name__ == '__main__':
    main()

