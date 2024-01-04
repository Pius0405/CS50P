import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        break

name_list = p.join(names)
print('Adieu, adieu, to',name_list)


