"""This module contains functions and variables related to the 
    player's health.

Functions:
    get()
    decrease(value)
    increase(value)
        
Global Variables:
    _player_info (dict)
"""

# Import modules
import types


# Global variables
_player_info = {"Player_1": 10} 
# Used a dictionary to allow for future player expansion


# Functions
def get():
    """Retrieves the player's health.

    Returns:
        (int): The player's health
    """
    return _player_info["Player_1"]


def decrease(value):
    """Reduces the player's health.

    Parameters:
        value (int): The amount of health to be reduced
    """
    global _player_info
    _player_info["Player_1"] -= value


def increase(value):
    """Increases the player's health.

    Parameters:
        (int): The amount of health to be increased
    """
    global _player_info
    _player_info["Player_1"] += value
