"""
The difference between the square of the sum and the sum of the squares of the first N natural numbers
module.
"""
def square_of_sum(number):
    """
    This function calculates the square of the sum of 1 to number
    :param number(int)
    :return sum(int)
    """
    square_sum = 0
    for digit in range(1, number + 1):
        square_sum += digit
    return square_sum ** 2


def sum_of_squares(number):
    """
    This function calculates the sum of square of 1 to number
    :param number(int)
    :return sum(int)
    """
    sum_square = 0
    for digit in range(1, number + 1):
        sum_square += digit ** 2
    return sum_square


def difference_of_squares(number):
    """
    This function calculates the diffence between he square of 
    the sum of the first ten natural numbers and the sum of 
    the squares of 1 to number and return a positive number
    :param number(int)
    :return (int)
    """
    if sum_of_squares(number) - square_of_sum(number) > 0:
        return sum_of_squares(number) - square_of_sum(number)
    return square_of_sum(number) - sum_of_squares(number)
