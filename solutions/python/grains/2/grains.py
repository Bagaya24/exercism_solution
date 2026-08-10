"""
Module of calculae the number of grains of wheat on a chessboard
"""

def square(number: int) -> int:
    """
    This function calculate the total number of grains
    on the chessboard on a given square
    :param number(int)
    :return grains(int)
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)


def total() -> int:
    """
    This function calculate the total number of grains
    on the chessboard
    :return grains(int)
    """
    grains = 0
    for i in range(64):
        grains += 2 ** i
    return grains
