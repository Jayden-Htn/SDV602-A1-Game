"""_summary_

Take string containing a proposed command produce a list of tokens
"""

_vocab_tokens = set(['north', 'south', 'east', 'west', 'fight', 'escape', 'pick',
                    'run', 'dodge', 'hide', 'swing'])

_operators = set(['+', '-', 'x', '/', '(', ')'])


def valid_list(p_input_string):
    """
    Takes a string, that is a sequence of command and operators 
    separated by "white space" characaters 
    returns a list of valid tokens - in order 

    Args:
        p_input_string (string): a string of characters 
    """
     
    result = []
    for string in p_input_string.split():
        if string.lower() in _vocab_tokens or string in _operators:
            result += [string]
    return result


if __name__ == "__main__":
    # tests
    print(valid_list('north south'))
