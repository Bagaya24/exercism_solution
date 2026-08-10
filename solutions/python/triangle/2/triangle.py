"""
Module of verifie triangle 
"""
def equilateral(sides:list) -> bool:
    """
    Verifi if a triangle is equilateral
    :param sides(list): a list of the sides of the triangle
    :return bool
    """
    side_1, side_2, side_3 = sides
    if side_1 == side_2 == side_3:
        if 0 in sides:
            return False
        return True
    return False



def isosceles(sides: list) -> bool:
    """
    Verifie if a triangle is isosceles
    :param sides(list):  a list if the sides of the triange
    :return bool
    """
    side_1, side_2, side_3 = sides
    if side_1 == side_2 and side_1 + side_2 >= side_3:
        return True
    if side_1 == side_3 and side_1 + side_3 >= side_2:
        return True
    if side_2 == side_3 and side_2 + side_3 >= side_1:
        return True
    return False


def scalene(sides: list) -> bool:
    """
    Verifie if a triangle is scalene
    :param sides(list): a list of the sides of the triangle
    :return bool
    """
    side_1, side_2, side_3 = sides
    if side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
        if side_1 + side_2 >= side_3 and side_1 + side_3 >= side_2 and side_2 + side_3 >= side_1:
            return True
        return False
    return False