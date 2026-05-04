"""
The Two Fer module
"""
def two_fer(name: str = None) -> str:
    """
    Function of Two Fer
    :param name(str)
    :return str
    """
    return f"One for {name if name else 'you'}, one for me."
