"""
This module contains functions and variables related to the player's inventory.

Functions:
    collect_item(item_name)
    remove_item(item_name)
    has_item(item_name)
    display_inventory()
    
Global Variables:
    _player_inventory (set)
"""

# Global variables
_player_inventory = set()


# Functions
def collect_item(item_name):
    """
    Adds an item to the player's inventory.

    Parameters:
        item_name (str): The name of the item to be added
    """
    _player_inventory.add(item_name)


def remove_item(item_name):
    """
    Removes an item from the player's inventory.

    Parameters:
        item_name (str): The name of the item to be removed
    """
    _player_inventory.remove(item_name)


def has_item(item_name):
    """
    Checks if the player has an item.

    Parameters:
        item_name (str): The name of the item to be checked

    Returns:
        (bool): True if the player has the item, False otherwise
    """
    return item_name in _player_inventory


def display_inventory():
    """
    Displays the player's inventory.

    Returns:
        result (str): The player's inventory
    """
    result = "Inventory:\n"
    for item in _player_inventory:
        result += "- " + item + "\n"
    if len(_player_inventory) == 0:
        result += "Empty\n"
    return result
