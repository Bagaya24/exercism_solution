"""
The encoded color resistor module
"""
def label(colors:list) -> str:
    """
    This function determines the encoded color of the 3 first colors of a resistors
    :param colors(list)
    :return result(str)
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
    prefix = {
        "gigaohms": 1_000_000_000,
        "megaohms": 1_000_000,
        "kiloohms": 1_000
    }
    result = ""
    for index, color in enumerate(colors):
        if index < 2:
            result += str(encoded_colors.get(color))
        else:
            result = int(result) * 10 ** encoded_colors.get(color)
            break

    for pre, val in prefix.items():
        if result // val >= 1:
            return f"{int(result/val)} {pre}"
    return f"{result} ohms"
