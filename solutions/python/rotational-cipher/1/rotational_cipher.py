"""
The Caeser cipher module
"""

import string
def rotate(text, key):
    """
    This function shifts all the letter in the alphabet using the key
    :param text: 
    :param key: 
    :return: result
    """
    low_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    result = "" 
    for letter in text:
        if letter.islower():
            index = low_alphabet.index(letter)
            new_index = (index + key) % 26
            new_letter = low_alphabet[new_index]
            result += new_letter
        elif letter.isupper():
            index = upper_alphabet.index(letter)
            new_index = (index + key) % 26
            new_letter = upper_alphabet[new_index]
            result += new_letter
        else:
            result += letter
    return result
