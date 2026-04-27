"""
The binary search algorithm
"""
def find(search_list, value):
    """
    This function searchs in a list a value by binary search algorithm
    :param search_list(list)
    :param value(int)
    :return mid: the index of the value in the search_list
    """
    if value in search_list:
        left = 0
        right =  len(search_list)
        while True:
            mid = (left + right) // 2
            if search_list[mid] > value:
                right = mid
            elif search_list[mid] < value:
                left = mid + 1
            else:
                return mid
            
            
    raise ValueError("value not in array")
