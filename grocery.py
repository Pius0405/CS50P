groceries_dict = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item not in groceries_dict:
            groceries_dict.update({item:1})
        else:
            try:
                groceries_dict[item] += 1
            except KeyError:
                pass

key_list = sorted(list(groceries_dict))
for item in key_list:
    print(str(groceries_dict[item]),item)


