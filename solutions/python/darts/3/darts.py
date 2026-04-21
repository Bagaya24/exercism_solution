"""
Module of the Darts game
"""
def score(coord_x:int, coord_y:int) -> int:
    """
    This function calculate the poins scored in a single toss of a 
    darts game by using the coordoates x and y of a concentric circle
    :param x(int)
    :param y(int)
    :return int
    """
    radius = coord_x ** 2 + coord_y ** 2
    outer_circle = 100
    middle_circle = 25
    inner_circle = 1
    if radius <= outer_circle:
        if radius <= inner_circle:
            return 10
        if radius <= middle_circle:
            return 5
        return 1
    return 0
