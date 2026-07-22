"""
 Module of implementation of the Atbash ciphe
"""
PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"
def encode(plain_text):
    """
    Encode to Atbash cipher
    param plain_text: str
    return str
    """
    encoded_text = ""
    plain_text_no_space = plain_text.replace(" ", "")
    number_char = 0
    for char in plain_text_no_space:
        
        if char.isdigit():
            if number_char % 5 == 0:
                encoded_text += " "
            encoded_text += char
            number_char += 1
        if char.lower() in PLAIN:
            if number_char % 5 == 0:
                encoded_text += " "
            index_char = PLAIN.index(char.lower())
            cipher_char = CIPHER[index_char]
            encoded_text += cipher_char
            number_char += 1
        
    return encoded_text.lstrip()


def decode(ciphered_text):
    """
    decode to Atbash cipher
    param ciphered_text
    return str
    """
    decoded_text = ""
    ciphered_text_no_space = ciphered_text.replace(" ", "")
    for char in ciphered_text_no_space:
        if char.isdigit():
            decoded_text += char
        else:
            index_cipher = CIPHER.index(char.lower())
            plain_char = PLAIN[index_cipher]
        
            decoded_text += plain_char
    return decoded_text
