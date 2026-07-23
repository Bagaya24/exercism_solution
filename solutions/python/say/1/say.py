"""
Module of translating number to English words
"""
def say(number: int) -> str:
    """
      Number to English words
    :param n: int
    :return: str
    """

    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"

    units = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    scales = ["", "thousand", "million", "billion"]

    def helper(num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return units[num] + " "
        elif num < 100:
            return tens[num // 10] + ("-" if num % 10 != 0 else " ") + helper(num % 10)
        elif num < 1000:
            return units[num // 100] + " hundred " + helper(num % 100)
        else:
            for index, scale in enumerate(scales[1:], 1):
                if num < 1000**(index + 1):
                    return helper(num // (1000**index)) + scale + " " + helper(num % (1000**index))
        return ""
    return helper(number).strip()

