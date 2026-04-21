import string
import re

def is_pangram(sentence: str) -> bool:
    """
    This function figures out if a sentence is pangram
    A pangram is a sentence using every letter of the 
    alphabet at least once. It is case insensitive, 
    so it doesn't matter if a letter is lower-case 
    (e.g. k) or upper-case (e.g. K).
    :param sentence(str)
    :return bool
    """
    alphabet = string.ascii_lowercase
    letters = re.findall(r'[a-zA-Z]+', sentence.lower())
    letters = "".join(letters)
    set_letters = set(letters)
    letters = "".join(sorted(set_letters))
    
    if alphabet == letters:
        return True
    return False