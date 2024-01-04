amount_due = 50
denomination = [25,10,5]
while amount_due > 0:
    print('Amount Due:',str(amount_due))
    coin = int(input('Insert Coin: '))
    if coin in denomination:
        amount_due -= coin
print('Change Owed:',str(amount_due*-1))

