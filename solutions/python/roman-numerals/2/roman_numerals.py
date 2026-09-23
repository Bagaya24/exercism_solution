"""
This module converts number from Arabic numbers to Roman numerals
"""

def roman(number: int) -> str:  
    
    """
    This function converts number from Arabic numbers to Roman numerals
    params: number(int)
    return str
    """
    roman_numeral = {
        1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I"
    }
    response = ""
    while number > 0:
        if number >= 1000:
            response += roman_numeral.get(1000)
            number -= 1000
        elif 500 <= number < 1000:
            response += roman_numeral.get(500)
            number -= 500
        elif 100 <= number < 500:
            response += roman_numeral.get(100)
            number -= 100
        elif 50 <= number < 100:
            response += roman_numeral.get(50)
            number -= 50
        elif 10 <= number < 50:
            response += roman_numeral.get(10)
            number -= 10
        elif 5 <= number < 10:
            response += roman_numeral.get(5)
            number -= 5
        else:
            response += roman_numeral.get(1)
            number -= 1

        if "VIIII" in response:
            response = response.replace("VIIII", "IX")
        elif "IIII" in response:
            response = response.replace("IIII", "IV")
        
        if "LXXXX" in response:
            response = response.replace("LXXXX", "XC")
        elif "XXXX" in response:
            response = response.replace("XXXX", "XL")
        
        if "DCCCC" in response:
            response = response.replace("DCCCC", "CM")
        elif "CCCC" in response:
            response = response.replace("CCCC", "CD")
        
    return response
