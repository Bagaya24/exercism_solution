"""
Convert a phrase to its acronym
"""
import re
def abbreviate(words:str) -> str:
    """
    Convert a phrase to its acronym
    param words: str
    return acronym: str
    """
    words_separed = re.split(r"[-\s_]+", words)
    acronym = ""
    for word in words_separed:
        acronym += word[0].upper()
    return acronym
