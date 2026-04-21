"""
Module of Nicomachus's classification
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 :
        raise ValueError("Classification is only possible for positive integers.")
    aliquots = []
    for aliquot in range(1, number):
        if number % aliquot == 0:
            aliquots.append(aliquot)

    if sum(aliquots) == number:
        return "perfect"
    if sum(aliquots) > number:
        return "abundant"
    return "deficient"
