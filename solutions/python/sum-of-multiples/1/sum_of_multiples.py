"""
The sum of multiples modules
"""
def sum_of_multiples(limit, multiples):
    """
    Function calculates the energy points earned by the player
    """
    multiples_list = [number for number in range(1, limit) if any(number % multiple == 0 for multiple in multiples if multiple != 0)]
    multiples_set = set(multiples_list)
    return sum(multiples_set)
