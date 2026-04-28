"""
The flatten array module
"""
def flatten(iterable):
    """
    This function takes a nested array of any depth and return a fully
    flattened array with no null like value 
    :param iterable(list)
    :return result(list)
    """
    result = []
    for track in iterable:
        if isinstance(track, list):
            result.extend(flatten(track))
        else:
            if track is not None:
                result.append(track)
    return result
