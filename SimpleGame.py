""" 
The main module of the game.  This module will be responsible for the game loop and the game window.
"""

import PySimpleGUI as psg
import command_parser.command_manager as CMD
import psg_reskinner as psg_rs


# initialise game states
current_location = 'Forest'
game_state = 'Movement' # movement, decision, combat
player = {'MaxHealth': 10, 'CurrentHealth': 10, 'Actions': [{'Name': 'Fist', 'Result': 2}, {'Name': 'Dodge', 'Result': 'No'}], 'Inventory': {}}
game_locations = {
    'Forest': {'Story': 'You are in the forest.\n- To the north is a cave.\n- To the east is the coast.\n- To the south is a castle.\n- To the west is a swamp.',
            'North': 'Castle','East': 'Coast', 'South': 'Cave', 'West': 'Swamp', 
            'Boss': 'Nymph', 'Image': 'forest.png', 'Theme': 'DarkGreen'},
    'Castle': {'Story': 'You are at the castle.\n- To the south is forest.',
            'North': '','East': '', 'South': 'Forest', 'West': '', 
            'Boss': 'Vampire', 'Image': 'castle.png', 'Theme': 'Reddit'},
    'Coast': {'Story': 'You are at the coast.\n- To the west is the forest.',
            'North': '','East': '', 'South': '', 'West': 'Forest', 
            'Boss': 'Serpent', 'Image': 'coast.png', 'Theme': 'LightBrown11'},
    'Cave': {'Story': 'You are at the cave.\n- To the north is forest.',
            'North': 'Forest','East': '', 'South': '', 'West': '', 
            'Boss': 'Spider', 'Image': 'cave.png', 'Theme': 'DarkBlack1'},
    'Swamp': {'Story': 'You are in the swamp.\n- To the east is the forest.',
            'North': '','East': 'Forest', 'South': '', 'West': '', 
            'Boss': 'Crocodile', 'Image': 'swamp.png', 'Theme': 'DarkGreen1'},
    }
game_bosses = {
    'Nymph': {'Description': 'Returning to the quiet of the forest, you breath a deep sigh of relief... until you see the nymph, who is obviously upset that you are disrupting the quiet of the forest.\n\n- Fight\n- Escape', 
              'EscapeMessage': 'Afraid to anger any more spirits, you promptly depart the area', 'FightMessage': 'Unafraid, you prepare to fight the nymph.',
                'Defeated': False, 'Health': 20, 'Attacks': [{}]},
    'Vampire': {'Description': 'Arriving at the castle, you  step foot through the grand entrance. Gazing aroung the elaborate foyer, your eyes set on the looming shape of a vampire, standing at the top of the staircase.\n\n- Fight\n- Escape', 
                'EscapeMessage': 'Absolutely terrified, you sprint out of the castle, hoping the vampire won\'t follow you.', 'FightMessage': 'Excitement ripples throughout your body as you prepare to battle the vampire.',
                'Defeated': False, 'Health': 20, 'Attacks': [{}]},
    'Serpent': {'Description': 'Hot from a long day of travel, you decide to cool down with a quick swim. Wading through the cool water, you soon feel something strong wrap around your ankle.\n\n- Fight\n- Escape', 
                'EscapeMessage': 'Instictually, you jank your foot free and race for the shore.', 'FightMessage': 'Never one to back down from a fight, you prepare to battle the serpent.',
                'Defeated': False, 'Health': 20, 'Attacks': [{}]},
    'Spider': {'Description': 'Flaming torch in hand, you work your way through the narrow cave passageway. Eventually, the walls open up into a large chamber, where a ginormous spider sits among its web.\n\n- Fight\n- Escape', 
                'EscapeMessage': 'The crawling heap of spiders sends shivers down your spine as you race back out through the tunnels.', 'FightMessage': 'You\'ve never been afraid of spiders, and you\'re not about to start now. You prepare to fight.',
                'Defeated': False, 'Health': 20, 'Attacks': [{}]},
    'Crocodile': {'Description': 'Wading through the patchy swamp, the soft ground keeps giving way, making you sink in deeper. Just as your foot becomes stuck in the mud, you see the head of a large crocodile nearby, staring at you.\n\n- Fight\n- Escape', 
                'EscapeMessage': '', 'FightMessage': 'You\'ve fought a crocodile before. Sure, this one might be twice the size, but you\'re not afraid. You prepare to fight.',
                'Defeated': False, 'Health': 20, 'Attacks': [{}]},

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
                psg.Text(CMD.show_current_place(game_locations, current_location), size=(40, 10), font='Any 12', 
                key='-OUTPUT-')], [command_col]] # size is the width and height of the story text box
    return psg.Window('Adventure Game', layout, size=(700, 400))


if __name__ == "__main__":
    # Start window
    window = make_a_window()

    # Main game loop
    while True:
        event, values = window.read()
        if event == 'Enter':
            # send input for processing and return new story
            input_value = values['-IN-'].lower()
            current_info = CMD.game_play(input_value, game_locations, current_location, game_state, player, game_bosses)
            # update global states
            game_state = current_info[2]
            # update GUI
            current_location = current_info[1]
            window['-OUTPUT-'].update(current_info[0])
            window['-IMG-'].update(r'images/'+game_locations[current_info[1]]
                                   ['Image'], size=(300, 300))
            # update background with psg_rs
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

