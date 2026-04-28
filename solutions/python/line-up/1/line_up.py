"""
The module of ...
"""
def line_up(name, number):
    """
    This function takes a given name and number and produces a sentence
    using that name and number as an ordinal numeral.
    Numbers ending in 1 (unless ending in 11) → "st"
    Numbers ending in 2 (unless ending in 12) → "nd"
    Numbers ending in 3 (unless ending in 13) → "rd"
    All other numbers → "th"
    :param name(str) 
    :param number(int) 
    :return: the final sentence 
    """
    if not 0 < number < 999:
        raise ValueError("The number must be betwenn 1 and 999")

    ending = ""
    two_ending = ""
    number = str(number)

    if len(number) > 1:
        two_ending = number[-2:]

    if number.endswith("1") and two_ending != "11":
        ending = "st"
    elif number.endswith("2") and two_ending != "12":
        ending = "nd"
    elif number.endswith("3") and two_ending != "13":
        ending = "rd"
    else:
        ending = "th"
    return "{name}, you are the {number}{ending} customer we serve today. Thank you!".format(name=name, number=number, ending=ending)


print(line_up("Mary", 122))

