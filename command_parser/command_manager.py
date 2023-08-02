"""_summary_

Handle the game play by processing commands.
"""

import command_parser.token_handler as TKN


def show_current_place(_game_locations, _current_location):
    """Gets the story at the current_location place

    Returns:
        string: the story at the current place
    """

    return _game_locations[_current_location]['Story']


def game_play(_inputs, _game_locations, _current_location, _game_state):
    """
    Runs the game_play

    Args:
        direction string: north, south, east or west

    Returns:
        string: the story at the current place and current location
    """

    list_of_tokens = TKN.valid_list(_inputs)
    for _token in list_of_tokens:
        if _game_state == 'movement':
            if _token.lower() in set(['north', 'south', 'east', 'west']):
                game_location = _game_locations[_current_location]
                proposed_location = game_location[_token.capitalize()]
                if proposed_location == '':
                    return ['You can not go that way.\n\n'+_game_locations[_current_location]['Story'], _current_location]
                else:
                    new_location = proposed_location
                    return [_game_locations[new_location]['Story'], new_location]
    return ['Invalid command.\n\n'+_game_locations[_current_location]['Story'], _current_location]
        

if __name__ == "__main__":
    # tests
    print(show_current_place({'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}}, 'Forest'))
    print(game_play('north', {'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}, 
            'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 'Image': 'castle.png'},}, 'Forest'))
    