def sym_dif(*args):
    list_item = list()
    for item in args:
        list_item += item
    
    unique_item = list()
    count_item = dict((item, list_item.count(item)) for item in sorted(list_item))
    for key, val in count_item.items():
        if val == 1:
            unique_item.append(key)

    return unique_item

print(sym_dif([1, 2, 3], [5, 2, 1, 4]))
