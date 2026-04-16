"""
Module the answer of Bob
"""

def response(hey_bob):
    """
    This function give the answer of Bob
    :param hey_bob(str)
    :return str
    """
    if hey_bob.rstrip().endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    return "Whatever."
