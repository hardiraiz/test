def to_dict(list_val):
    dict_val = dict()
    for item in list_val:
        dict_val[item[1]] = item[0]
    
    return dict_val


def update_inventory(list_1, list_2):
    cur_inv = to_dict(list_1)
    new_inv = to_dict(list_2)

    for key, val in new_inv.items():
        if key in cur_inv:
            cur_inv[key] += val
        else:
            cur_inv[key] = val

    cur_inv = [[v, k] for k, v in cur_inv.items()]
    
    return cur_inv


# Example inventory lists
cur_inv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

new_inv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

print(update_inventory(cur_inv, new_inv))
