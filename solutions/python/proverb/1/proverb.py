"""
The proverb modul
"""
def proverb(*args, qualifier=None):
    """
     This function take a given list of inputs and generate the relevant proverb.
    For example, given the list: ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
     For want of a nail the shoe was lost.
    For want of a shoe the horse was lost.
    For want of a horse the rider was lost.
    For want of a rider the message was lost.
    For want of a message the battle was lost.
    For want of a battle the kingdom was lost.
    And all for the want of a nail.
    """
    results = []
    if len(args) == 1:
        results.append(f"And all for the want of a{' '+qualifier if qualifier else ''} {args[0]}.")
        return results
        
    if len(args) == 0:
        return []

    second_args = list(args)
    element = second_args.pop(0)
    
    if len(args) == 2:
        second_args.insert(1, element)
    else:   
        second_args.insert(len(args) - 1, element)
    
    index = 1
    for word1,word2 in zip(args, second_args):
        if index == len(args):
            results.append(f"And all for the want of a{' '+qualifier if qualifier else ''} {word2}.")
            continue
            
        results.append(f"For want of a {word1} the {word2} was lost.")
        index += 1
    return results