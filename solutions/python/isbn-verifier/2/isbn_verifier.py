"""
Module of ISBN-10 verification process
"""
def is_valid(isbn):
    """
       This function verifie the ISBN-10
       The ISBN-10 format is 9 digits (0 to 9) plus one check character 
       (either a digit or an X only).In the case the check character is 
       an X, this represents the value '10'. These may be communicated 
       with or without hyphens, and can be checked for their validity 
       by the following formula:(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ 
       * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
       :param isbn: str
       return bool
    """
    result = 0
    isbn_number = [number for number in isbn if number.isdigit() or number.isalpha()]
    if len(isbn_number) == 10:
        for digit,multi in zip(isbn_number, range(10, 0, -1)):
            if not digit.isdigit():
                if isbn_number.index(digit) == 9 and digit == "X":
                    digit = 10
                else:
                    return False
            result += int(digit) * multi
    
        if result % 11 == 0:
            return True
        return False
    return False
