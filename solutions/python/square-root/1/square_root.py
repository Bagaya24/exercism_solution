"""
The Square Root module
"""
def square_root(number : int) -> int:
    """
    Function calculates the square root of a given number.
    :param number(int)
    :return int
    """
    for num in range(0, number + 1):
        if num * num == number:
            return num
