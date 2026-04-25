"""
The secret handshake module
"""
def commands(binary_str):
    """
    This function converts a number between 1 and 31 to a sequence of actions
    eg:
    00001 = wink
    00010 = double blink
    00100 = close your eyes
    01000 = jump
    10000 = Reverse the order of the operations in the secret handshake.
    :param binary_str(str)
    :return actions(list)
    """
    actions = []
    for index,digit in enumerate(binary_str[::-1]):
        if digit == "1":
            if index == 0:
                actions.append("wink")
            elif index == 1:
                actions.append("double blink")
            elif index == 2:
                actions.append("close your eyes")
            elif index == 3:
                actions.append("jump")
            else:
                actions = actions[::-1]
    return actions
            
    
