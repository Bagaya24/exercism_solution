def append(list1, list2):
    
    return list1 + list2


def concat(lists):
    result = []
    for array in lists:
        if isinstance(array, list):
            for array2 in array:
                result.append(array2)
        else:
            result.append(array)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    for item in list:
        initial = (function(initial, item))
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = (function(initial, item))
    return initial


def reverse(list):
    return list[::-1]
