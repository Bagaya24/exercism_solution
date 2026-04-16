def equilateral(sides:list) -> bool: 
    a, b, c = sides
    if a == b == c:
        if 0 in sides:
            return False
        return True
    return False



def isosceles(sides: list) -> bool:
    a, b, c = sides
    if a == b and a + b >= c:
        return True
    if a == c and a+c >= b:
        return True
    if b == c and b+c >= a:
        return True
    return False


def scalene(sides: list) -> bool:
    a, b, c = sides
    if a != b and a != c and b != c:
        if a + b >= c and a + c >= b and b + c >= a:
            return True
        return False
    return False