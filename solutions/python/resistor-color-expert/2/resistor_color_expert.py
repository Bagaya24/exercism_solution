"""
The encoded colors of a resistor module
"""
def resistor_label(colors):
    """
    This function determines the encoded colors of a resistor
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
    tolerance = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    tolerance_value = 0
    result = ""
    if len(colors) <= 4:
        
        for index, color in enumerate(colors):
            if index == 3:
                tolerance_value = tolerance.get(color)
                break
            elif index == 2:
                result = int(result) * 10 ** encoded_colors.get(color)
            else:
                result += str(encoded_colors.get(color))
    else:
        for index, color in enumerate(colors):
            if index == 4:
                tolerance_value = tolerance.get(color)
                break
            elif index == 3:
                result = int(result) * 10 ** encoded_colors.get(color)
            else:
                result += str(encoded_colors.get(color))

    for pref, val in prefix.items():
        if int(result) / val >= 1:
            result = int(result) / val
            
            return f"{int(result) if result.is_integer() else result} {pref} ±{tolerance_value}%"
    return f"{result} ohms{"" if tolerance_value == 0 else f" ±{tolerance_value}%"}"

