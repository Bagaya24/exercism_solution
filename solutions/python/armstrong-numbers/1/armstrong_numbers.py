"""
Module that find the Armstrong number
"""

def is_armstrong_number(number:int) -> bool:
    """
    This function find the Armstrong number
    :param number(int)
    :return boolean
    """
    str_number = str(number)
    pwd = len(str_number)
    total = 0
    for digit in str_number:
        total += int(digit) ** pwd
    if total == number:
        return True
    return False
