"""
The module of reformating a dictionnary
"""
def transform(legacy_data: dict) -> dict:
    """
    This function changes the data format of letters and their point values in the game.
    Currently, letters are stored in groups based on their score, in a one-to-many mapping.

    1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
    2 points: "D", "G",
    3 points: "B", "C", "M", "P",
    4 points: "F", "H", "V", "W", "Y",
    5 points: "K",
    8 points: "J", "X",
    10 points: "Q", "Z",
    This needs to be changed to store each individual letter with its score in a one-to-one mapping.

    "a" is worth 1 point.
    "b" is worth 3 points.
    "c" is worth 3 points.
    "d" is worth 2 points.
    :params legacy_data(dict)
    """
    new_legacy_data = {}
    for key, value in legacy_data.items():
        for letter in value:
            new_legacy_data.setdefault(letter.lower(), key)

    new_legacy_data = dict(sorted(new_legacy_data.items()))
    return new_legacy_data
