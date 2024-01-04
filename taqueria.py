taco_price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        taco = input('Item: ')
    except EOFError:
        print()
        break
    else:
        try:
            total += taco_price[taco.title()]
            print(f'Total: ${total:.2f}')
        except KeyError:
            pass



