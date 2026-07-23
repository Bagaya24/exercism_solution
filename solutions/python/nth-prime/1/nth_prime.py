"""
Given a number n, determine what the nth prime is.
"""
def prime(number:int) -> int | None:
    """
    determine what the nth prime is the number
    param: number
    return candidate 
    """
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    if number == 1:
        return 2

    count = 1 
    candidate = 3

    while count < number:
        if is_prime(candidate):
            count += 1
            if count == number:
                return candidate
        candidate += 2 
    return None


def is_prime(num:int) -> bool:
    """
    Determine if the num is a prime number
    param: num
    return boolean
    """
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

 
    divider = 5
    while divider * divider <= num:
        if num % divider == 0 or num % (divider + 2) == 0:
            return False
        divider += 6
    return True
