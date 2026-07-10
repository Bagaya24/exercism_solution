"""
The module of the translator text from English to Pig Latin
"""

def translate(text:str) -> str:
    """
        The translator text from English to Pig Latin
    """
    vowels = tuple("aeiou")
    consonants = tuple("bcdfghjklmnpqrstvwxyz")

    words = text.split()
    final_words = ""
    for index, word in enumerate(words):
        # Rules 1
        if word.startswith(vowels) or text[:2] == "xr" or text[:2] == "yt":
            word = word + "ay"
            final_words += " " + word if index != 0 else word
            continue

        # Rules 2
        if word.startswith(consonants):
            is_y_first = False
            while word.startswith(consonants):
                # Rules 3
                if word[:2] == "qu":
                    qu = word[:2]
                    word += qu
                    word = word.replace(qu, "", 1)
                    break
                # Rules 4
                if word.startswith("y") and is_y_first:
                    break
                consonant = word[0]
                word += consonant
                word = word.replace(consonant, "", 1)
                is_y_first = True
            word = word + "ay"
            final_words += " " + word if index != 0 else word
            continue

    return final_words
