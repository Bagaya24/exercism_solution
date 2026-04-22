"""
Module of isogram
"""
import re

def is_isogram(string):
    """
    This function determines if a word or phrase is an isogram.
    :param string: str
    :return bool
    """
    letters = re.findall(r'[a-zA-Z]+', string.lower())
    len_set_letters = len(set("".join(letters)))
    len_letters = len("".join(letters))
    if len_letters == len_set_letters:
        return True
    return False
    
