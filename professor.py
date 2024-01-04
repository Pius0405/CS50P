import random

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        for i in range(3):
            try:
                ans = int(input(f'{X} + {Y} = '))
                if ans == X + Y:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print('EEE')
                if i == 2:
                    print(f'{X} + {Y} = {X+Y}')
    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case _:
            return random.randint(100,999)


if __name__ == "__main__":
    main()
