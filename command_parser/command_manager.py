"""_summary_

Handle the game play by processing commands.
"""


def show_current_place(_game_locations, _current_location):
    """Gets the story at the current_location place

    Returns:
        string: the story at the current place
    """

    return _game_locations[_current_location]['Story']


def game_play(_direction, _game_locations, _current_location):
    """
    Runs the game_play

    Args:
        direction string: north, south, east or west

    Returns:
        string: the story at the current place and current location
    """

    if _direction.lower() in set(['north', 'south', 'east', 'west']):
        game_location = _game_locations[_current_location]
        print("GL", game_location)
        print("D", _direction.capitalize())
        proposed_location = game_location[_direction.capitalize()]
        print("PL", proposed_location)
        if proposed_location == '':
            print('You can not go that way.')
            return ['You can not go that way.\n'+_game_locations[_current_location]['Story'], _current_location]
        else:
            new_location = proposed_location
            return [_game_locations[new_location]['Story'], new_location]