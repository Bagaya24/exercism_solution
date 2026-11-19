"""
The scrabble module
"""
def score(word):
    """
    This function can compute a word's Scrabble score by summing the values of its letters.
    """
    letter_value = {
        "A,E,I,O,U,L,N,R,S,T": 1,
        "D, G": 2,
        "B,C,M,P": 3,
        "F,H,V,W,Y": 4,
        "K": 5,
        "J,X": 8,
        "Q,Z": 10
    }
    result = 0
    for letter in word:
        for letters, value in letter_value.items():
            if letter.upper() in letters:
                result += value
    return result