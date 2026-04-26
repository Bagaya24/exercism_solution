"""
The module of anagram
"""
def find_anagrams(word: str, candidates: list) -> str:
    """
    This function takes a given word and one or more candidate words and
    find the candidates that are anagrams of the target word
    :param word(str) : the target
    :param candidates(list)
    :return anagram(list)
    """
    verification = []
    anagram = []
    word_list = list(word.lower())
    for candidate in candidates:
        if len(candidate) == len(word) and candidate.lower() != word.lower():
            verification = [char.lower() for char in candidate if char.lower() in word.lower()]
        if len(verification) == len(word):
            if sorted(verification) == sorted(word_list):
                anagram.append(candidate)
        verification = []
    return anagram
