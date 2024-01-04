def main():
    name = input('camelCase: ')
    name = camel_to_snake(name)
    print(name)

def camel_to_snake(name):
    if name.islower():
        return name
    else:
        snake_name = ''
        for char in name:
            if char.islower():
                snake_name = snake_name + char
            else:
                snake_name = snake_name + '_' + char.lower()
        return snake_name

main()
