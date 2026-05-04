"""
The Two Fer module
"""
def two_fer(name: str = None) -> str:
    """
    Function of Two Fer
    """
    if name is None:
        name = "you"
    return f"One for {name}, one for me."
