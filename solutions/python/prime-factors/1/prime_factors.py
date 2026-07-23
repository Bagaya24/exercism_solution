"""
The module of computing the prime factors of a given natural number
"""
def factors(value:int) -> list:
    """
    This function compute the prime factors of a given natural number.
    param: value(int): the natural number
    return: primes_numbers(list): list of the primes numbers
    """
    primes_numbers = []
    for n in range(2, value + 1):
        while value % n == 0:
            primes_numbers.append(n)
            value = value / n
        if value == 1:
            break
    return primes_numbers
