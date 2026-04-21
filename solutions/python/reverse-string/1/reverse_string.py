"""
Module of reverse a string
"""
def reverse(text:str) -> str:
    """
    This function revers strings
    :param text: str
    :return : str
    """
    letters = [letter for letter in text]
    return "".join(letters[::-1])
