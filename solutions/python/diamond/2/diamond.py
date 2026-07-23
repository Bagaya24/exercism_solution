"""
The module of the diamand kata
"""
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter:str)->list:
    """
    The function of the diamand kata
    param: letter(str)
    return : list
    """
    index_letter = ALPHABET.index(letter) + 1
    dot = index_letter + (index_letter - 1)
    diamond = []
    for index, row_num in enumerate(range(index_letter)):
        if index == 0:
            diamond.append(f"{' '*(int(dot / 2))}{ALPHABET[row_num]}{' '*(int(dot / 2))}")
        elif index == 1:
            diamond.append(f"{' '*(int(dot/2)-index)}{ALPHABET[row_num]}{' '*index}{ALPHABET[row_num]}{' '*(int(dot/2)-index)}")
        else:
            diamond.append(
                f"{' ' * (int(dot / 2) - index)}{ALPHABET[row_num]}{' ' * (index + (index - 1))}{ALPHABET[row_num]}{' ' * (int(dot / 2) - index)}")
    return diamond+diamond[0:-1][::-1]
    
