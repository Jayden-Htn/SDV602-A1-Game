""" 
The main module of the game.  This module will be responsible for the game loop and the game window.
"""

import PySimpleGUI as sg
import command_parser.token_handler as token_handler

# initialise game states
current_location = 'Forest'
game_locations = {
    'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png'},
    'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 'Image': 'castle.png'},
    'Coast': {'Story': 'You are at the coast.\n- To the west is the forest.',
            'North': '','East': '', 'South': '', 'West': 'Forest', 'Image': 'coast.png'},
    'Cave': {'Story': 'You are at the cave.\n- To the north is forest.',
            'North': 'Forest','East': '', 'South': '', 'West': '', 'Image': 'cave.png'},
    'Swamp': {'Story': 'You are in the swamp.\n- To the east is the forest.',
            'North': '','East': 'Forest', 'South': '', 'West': '', 'Image': 'swamp.png'},
    }


def show_current_place():
    """Gets the story at the current_location place

    Returns:
        string: the story at the current place
    """
    global current_location

    return game_locations[current_location]['Story']


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global current_location

    if direction.lower() in set(['north', 'south', 'east', 'west']):
        game_location = game_locations[current_location]
        proposed_location = game_location[direction.capitalize()]
        if proposed_location == '':
            return 'You can not go that way.\n'+game_locations[current_location]['Story']
        else:
            current_location = proposed_location
            return game_locations[current_location]['Story']


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Green')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(20, 1), font='Any 14', do_not_clear=False)]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/forest.png', size=(300, 300), key="-IMG-"), 
                sg.Text(show_current_place(), size=(100, 6), font='Any 12', 
                key='-OUTPUT-')], [command_col]]
    return sg.Window('Adventure Game', layout, size=(600, 400))


if __name__ == "__main__":
    # Start window
    window = make_a_window()

    # Main game loop
    while True:
        event, values = window.read()
        if event == 'Enter':
            list_of_tokens = token_handler.valid_list(values['-IN-'].lower())

            for token in list_of_tokens:
                current_story = game_play(token)
                window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+game_locations[current_location]
                                   ['Image'], size=(300, 300))
            pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else:
            pass

    window.close()
