"""
Module of encoded colors of resistors
"""
def color_code(color:str) -> int:
    """
    This function determines the value of the encoded color of a resistor
    :param color(str)
    """
    encoded_colors = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return encoded_colors.get(color)


def colors():
    """
    This function return the encoded colors of resistors
    """
    return [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
