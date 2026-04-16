"""
Module of Raindrops
"""
def convert(number):
    """
    This function convert a number into
    its corresponding raindrop sounds.
    If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
    :params number(int)
    :return str
    """
    raindrop_sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    sound = ""
    for key, value in raindrop_sounds.items():
        if number % key == 0:
            sound += value
    if sound == "":
        return str(number)
    return sound