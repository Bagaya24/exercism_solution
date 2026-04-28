"""
The Hamming distance between two DNA strands module
"""
def distance(strand_a, strand_b):
    """
    This function calculates the Hamming distance between two DNA strands.
    :param strand_a(str)
    :param strand_b(str)
    :return count(int)
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0
    for str_a, str_b in zip(strand_a, strand_b):
        if str_a != str_b:
            count += 1
    return count
