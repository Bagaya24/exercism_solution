"""
Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.
"""

def slices(series, length):
    """
Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.
    :param series: 
    :param length: 
    :return: substrings
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    substrings = []

    for digit in range(len(series) - length + 1):
        substrings.append(series[digit : digit + length])
    return substrings