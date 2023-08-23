"""
This module contains functions and variables related to the player's health.

Functions:
    get()
    decrease(value)
    increase(value)
        
Global Variables:
    _health_value (int)
"""

# Import modules
import types


# Global variables
_health_value: int = 10


# Functions
def get():
    """
    Retrieves the player's health.

    Returns:
        _health_value (int): The player's health
    """
    return _health_value


def decrease(value):
    """
    Reduces the player's health.

    Parameters:
        value (int): The amount of health to be reduced
    """
    global _health_value
    _health_value -= value


def increase(value):
    """
    Increases the player's health.

    Parameters:
        value (int): The amount of health to be increased
    """
    global _health_value
    _health_value += value
