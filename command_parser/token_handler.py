"""This module contains functions for validating tokens.

Functions:
    valid_list(p_input_string)
    
Global Variables:
    _vocab_tokens (set)
"""

# List of valid tokens
_vocab_tokens = set(
    [
        "north",
        "south",
        "east",
        "west",
        "fight",
        "escape",
        "fist",
        "sword",
        "pickup",
        "enter",
        "talk",
        "leave",
        "search",
        "inventory",
        "crystal",
    ]
)


# Functions
def valid_list(p_input_string):
    """Take string containing a proposed command produce a list of tokens.

    Parameters:
        p_input_string (str): The string to be tokenized.

    Returns:
        result (list): A list of valid tokens.
    """
    result = []
    for astring in p_input_string.split():
        if astring.lower() in _vocab_tokens:
            result += [astring]

    return result
