"""
The Two Fer module
"""
def two_fer(name: str | None = None) -> str:
    """
    Function of Two Fer
    :param name(str)
    :return str
    """
    return f"One for {name or 'you'}, one for me."
