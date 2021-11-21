from typing import Counter


def pairwise(arr, arg):
    result = list()
    for idx, num in enumerate(arr):
        len_arr = len(arr)-1
        if idx < len_arr:
            counter = idx+1
        else:
            counter = idx

        while len_arr >= counter:
            if num + arr[counter] == arg:
                # print(f'{num} + {arr[counter]} = {arg}')
                # print(f'append to list ({idx} + {counter})')
                result.append(idx+counter)
            counter += 1

    # print(result)
    return sum(result)


print(pairwise([1, 3, 2, 4], 4))
