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
def game_play(_inputs, _game_locations, _current_location, _game_state, _player, _bosses):
    """
    Runs the game_play

    Args:
        direction string: north, south, east or west

    Returns:
        string: the story at the current place and current location
    """

    list_of_tokens = TKN.valid_list(_inputs)
    _token = list_of_tokens[0]
    if _game_state == 'Movement':
        return_value = ['Invalid command.\n\n'+_game_locations[_current_location]['Story'], _current_location, _game_state]
    elif _game_state == 'Decision':
        return_value = ['Invalid command.\n\n'+_bosses[_game_locations[_current_location]['Boss']]['Description'], _current_location, _game_state]
    # return format: 'game story + message', 'current location', 'game state'
    print('Game state', _game_state)
    if _game_state == 'Movement':
        if _token.lower() in set(['north', 'south', 'east', 'west']):
            game_location = _game_locations[_current_location]
            proposed_location = game_location[_token.capitalize()]
            if proposed_location == '':
                return_value = ['You can not go that way.\n\n'+_game_locations[_current_location]['Story'], _current_location, _game_state]
            else:
                if _game_locations[proposed_location]['Boss'] == 'None' or _bosses[_game_locations[proposed_location]['Boss']]['Defeated']:
                    return_value =  [_game_locations[proposed_location]['Story'], proposed_location, _game_state]
                else:
                    _game_state = 'Decision'
                    return_value =  [_bosses[_game_locations[proposed_location]['Boss']]['Description'], proposed_location, _game_state]
    elif _game_state == 'Decision':
        if _token.lower() == 'fight':
            return_value =  [_bosses[_game_locations[_current_location]['Boss']]['FightMessage'], _current_location, 'Combat']
        if _token.lower() == 'escape':
            print('called')
            return_value =  [_bosses[_game_locations[_current_location]['Boss']]['EscapeMessage']+'\n\n'+_game_locations[_current_location]['Story'], _current_location, 'Movement']
    elif _game_state == 'Combat':
        if _token.lower() in set(['swing', 'dodge']):
            x += 1
    print('Returning')
    return return_value
        

if __name__ == "__main__":
    # tests
    print(show_current_place({'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}}, 'Forest'))
    print(game_play('north', {'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'}, 
            'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 'Image': 'castle.png'},}, 'Forest'))
    