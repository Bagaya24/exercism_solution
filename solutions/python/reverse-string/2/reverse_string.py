"""
Module of reverse a string
"""
def reverse(text:str) -> str:
    """
    This function revers strings
    :param text: str
    :return : str
    """
    letters = list(text)
    return "".join(letters[::-1])
