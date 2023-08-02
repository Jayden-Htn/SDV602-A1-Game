""" 
The main module of the game.  This module will be responsible for the game loop and the game window.
"""

import PySimpleGUI as psg
import command_parser.token_handler as TKN
import command_parser.command_manager as CMD
import psg_reskinner as psg_rs


# initialise game states
current_location = 'Forest'
game_locations = {
    'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 'Image': 'forest.png', 'Theme': 'DarkGreen'},
    'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 'Image': 'castle.png', 'Theme': 'Reddit'},
    'Coast': {'Story': 'You are at the coast.\n- To the west is the forest.',
            'North': '','East': '', 'South': '', 'West': 'Forest', 'Image': 'coast.png', 'Theme': 'LightBrown11'},
    'Cave': {'Story': 'You are at the cave.\n- To the north is forest.',
            'North': 'Forest','East': '', 'South': '', 'West': '', 'Image': 'cave.png', 'Theme': 'DarkBlack1'},
    'Swamp': {'Story': 'You are in the swamp.\n- To the east is the forest.',
            'North': '','East': 'Forest', 'South': '', 'West': '', 'Image': 'swamp.png', 'Theme': 'DarkGreen1'},
    }


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """
    global current_location
    global game_locations

    psg.theme('Dark Green')  # please make your windows
    prompt_input = [psg.Text('Enter your command', font='Any 14'), psg.Input(
        key='-IN-', size=(20, 1), font='Any 14', do_not_clear=False)]
    buttons = [psg.Button('Enter',  bind_return_key=True), psg.Button('Exit')]
    command_col = psg.Column([prompt_input, buttons], element_justification='r')
    layout = [[psg.Image(r'images/forest.png', size=(300, 300), key="-IMG-"), 
                psg.Text(CMD.show_current_place(game_locations, current_location), size=(100, 6), font='Any 12', 
                key='-OUTPUT-')], [command_col]]
    return psg.Window('Adventure Game', layout, size=(600, 400))


if __name__ == "__main__":
    # Start window
    window = make_a_window()

    # Main game loop
    while True:
        event, values = window.read()
        if event == 'Enter':
            list_of_tokens = TKN.valid_list(values['-IN-'].lower())

            for token in list_of_tokens:
                current_info = CMD.game_play(token, game_locations, current_location)
            current_location = current_info[1]
            window['-OUTPUT-'].update(current_info[0])
            window['-IMG-'].update(r'images/'+game_locations[current_info[1]]
                                   ['Image'], size=(300, 300))
            new_theme = game_locations[current_location]['Theme']
            psg_rs.animated_reskin(window=window,
                            new_theme=new_theme,
                            theme_function=psg.theme,
                            lf_table=psg.LOOK_AND_FEEL_TABLE,
                            duration=800,)
            pass
        elif event == 'Exit' or event is None or event == psg.WIN_CLOSED:
            break
        else:
            pass

    window.close()

