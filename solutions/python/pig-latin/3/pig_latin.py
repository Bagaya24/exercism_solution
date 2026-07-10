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
        pig_word = word
        # Rules 1
        if pig_word.startswith(vowels) or text[:2] == "xr" or text[:2] == "yt":
            pig_word = word + "ay"
            final_words += " " + pig_word if index != 0 else pig_word
            continue

        # Rules 2
        if pig_word.startswith(consonants):
            is_y_first = False
            while pig_word.startswith(consonants):
                # Rules 3
                if pig_word[:2] == "qu":
                    word_with_qu = pig_word[:2]
                    pig_word += word_with_qu
                    pig_word = pig_word.replace(word_with_qu, "", 1)
                    break
                # Rules 4
                if pig_word.startswith("y") and is_y_first:
                    break
                consonant = pig_word[0]
                pig_word += consonant
                pig_word = pig_word.replace(consonant, "", 1)
                is_y_first = True
            pig_word = pig_word + "ay"
            final_words += " " + pig_word if index != 0 else pig_word
            continue

    return final_words
