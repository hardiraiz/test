list_num = [1, 2, 3, 1, 3, 5, 4]
list_num = sorted(list_num)
b = dict((i, list_num.count(i)) for i in list_num)
print("Hello world!", b)
