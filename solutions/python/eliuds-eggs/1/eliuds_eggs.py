"""
The module of counting the number of 1 bits in the binary representation of a number
"""
def egg_count(display_value):
    """
    This function count the number of 1 bits in the binary representation of a number
    param: display_value(str)
    return : int
    """
    number_in_bin_str = ""
    while display_value > 1:
        rest = display_value % 2
        display_value = int(display_value/2)
        number_in_bin_str += str(rest)
        if display_value < 2:
            number_in_bin_str += str(display_value)
    return number_in_bin_str.count("1")
