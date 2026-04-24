"""
The encoded colors module
"""

def value(colors:list) -> int:
    """
    This function determines the two first colors of a encoded colors of the resistors
    :param colors(list): a list of colors
    :return result(int)
    """
    encoded_colors = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }
    result = ""
    for color_index in range(0, 2):
        result += encoded_colors.get(colors[color_index])
    return int(result)
