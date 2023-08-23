"""_summary_

Take string containing a proposed command produce a list of tokens
"""
_vocab_tokens = set(['north', 'south', 'east', 'west', 'fight', 'escape', 'fist', 
                     'sword', 'pickup', 'enter', 'talk', 'leave', 'search', 
                     'inventory', 'crystal'])


def valid_list(p_input_string):
    """
    Takes a string, that is a sequence of command and operators 
    separated by "white space" characaters 
    returns a list of valid tokens - in order 

    Args:
        p_input_string (string): a string of characters 
    """
    result = []
    for astring in p_input_string.split():
        if astring.lower() in _vocab_tokens:
            result += [astring]

    return result
