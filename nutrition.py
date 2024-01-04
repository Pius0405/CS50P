fruit_calories = {
    'apple':'130',
    'Avocado':'50',
    'banana':'110',
    'cantaloupe':'50',
    'grapefruit':'60',
    'grapes':'90',
    'honeydew melon':'50',
    'Kiwifruit':'90',
    'lemon':'15',
    'lime':'20',
    'nectarine':'60',
    'orange':'80',
    'peach':'60',
    'pear':'100',
    'pineapple':'50',
    'plums':'70',
    'strawberries':'50',
    'Sweet Cherries':'100',
    'tangerine':'50',
    'watermelon':'80'
}

key = input('Item: ')
if key in fruit_calories:
    print('Calories:',fruit_calories[key])

