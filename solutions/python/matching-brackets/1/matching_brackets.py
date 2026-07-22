"""
Sotware for the bracketeer
"""
def is_paired(input_string):
    """
    Bracketeer
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in input_string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:

            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0
