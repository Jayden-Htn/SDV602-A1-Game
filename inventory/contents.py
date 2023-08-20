"""_summary_

"""
_player_inventory = set()


def collect_item(item_name):
    _player_inventory.add(item_name)

def remove_item(item_name):
    _player_inventory.remove(item_name)

def has_item(item_name):
    return item_name in _player_inventory

def display_inventory():
    result = "Inventory:\n"
    for item in _player_inventory:
        result += item + "\n"
    if len(_player_inventory) == 0:
        result += "Empty"
    result += "\n"
    return result
