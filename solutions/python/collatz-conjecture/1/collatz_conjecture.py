"""
Module of Collatz Conjecture
"""
def steps(number):
    """
    This function do the Collatz Conjecture
    :param number(int)
    :return step(int) : The step the took the number to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (number *  3) + 1
        
        step += 1
    return step
