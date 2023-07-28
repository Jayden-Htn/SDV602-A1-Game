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
        

if __name__ == "__main__":
    # tests
    print(show_current_place({'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}}, 'Forest'))
    print(game_play('north', {'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}, 
            'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 'Image': 'castle.png'},}, 'Forest'))
    