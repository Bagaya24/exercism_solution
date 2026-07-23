"""
Run-length encoding (RLE)
"""


def decode(string:str)->str:
    """
    The decoder of RLE
    param: string
    return decoded
    """
    decoded = ""
    multiple = ""
    for char in string:
        if char.isdigit():
            multiple += char
        else:
            if multiple:
                decoded += int(multiple) * char
                multiple = ""
            else:
                decoded += char

    return decoded


def encode(string:str)->str:
    """
    The encoder of RLE
    param: string
    return encode
    """
    prev = ""
    count = 0
    encoded = ""
    for index, char in enumerate(string):
        if index == 0:
            prev = char
            count += 1
        elif char == prev:
            count += 1
            prev = char
        else:
            encoded += f'{count if count > 1 else ""}{prev}'
            count = 1
            prev = char
        if index == len(string) - 1:
            encoded += f'{count if count > 1 else ""}{prev}'
    return encoded
