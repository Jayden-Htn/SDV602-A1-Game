"""_summary_
Manages the commands - may not be the best name at this time

"""
# Import typing
import command_parser.token_handler as TKN
import inventory.contents as INV
import status.health as HP


# Game commands
def move(game_place, extra=''):
    """_summary_

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state
    
    location = game_place[1]
    game_state = location

    story_result = extra+show_current_place()

    return story_result


def pickup_key(game_place):
    """_summary_
        Find key in sand
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    INV.collect_item("key")
    return move(game_place, 'Picked up key.\n\n')

def pickup_sword(game_place):
    """_summary_
        Find sword in cave
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    INV.collect_item("sword")
    return move(game_place, 'Picked up sword.\n\n')


def enter_castle(game_place):
    result = ""
    if INV.has_item('key'):
        result = move(game_place)
    else:
        result = "The door is locked.\n"+show_current_place()
    return result

def talk_to_chief(game_place):
    result = ""
    if INV.has_item('crystal'):
        result = move(game_place)
    else:
        result = "Adventurer, please help us. An evil vampire has been attacking our village. Please help us.\n"+show_current_place()
    return result

def display_inventory(game_place):
    result = ""
    result = INV.display_inventory()+'\n'+show_current_place()
    return result

def fight(game_place):
    """
    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Implement "fight"
    # Check inventory for a sword - if no sword go to blacksmith
    # If there is a sword then flip a random to decide if they win or lose
    # If they lose they lose health
    #    They die when health is zero. When they die,  empty inventory, game_state = Forest
    # If they win they can move into the Castle ...
    result = "You can not fight because you don\'t have a sword.\nGet a sword from the blacksmith\'s.\nFighting has not been implemented\n Can you implement it?"+show_current_place()

    return result


game_state = 'Forest'
# format is {place: {story: string, action/direction: (action function, new state), ...}}
game_places = {'Forest': {'Story': 'You are in the forest.\n- To the north is a castle\n- To the east is the coast.\n- To the south is a cave.\n- To the west is a village.',
                          'North': (move, 'Castle'), 'East': (move, 'Coast'), 'South': (move, 'Cave'), 'West': (move, 'Village'),
                          'Image': 'forest.png', 'Theme': 'DarkGreen'},
                'Castle': {'Story': 'You are at the castle.\n- Enter the castle.\n- To the south is forest.',
                        'Enter': (enter_castle, 'InCastle'), 'South': (move, 'Forest'),
                        'Image': 'castle.png', 'Theme': 'Reddit'},
                'Coast': {'Story': 'You are at the coast.\n- Enter the water.\n- To the west is the forest.',
                          'Enter': (move, 'Ocean'), 'West': (move, 'Forest'),
                          'Image': 'coast.png', 'Theme': 'LightBrown11'},
                'Cave': {'Story': 'You are at the cave.\n- Enter the cave.\n- To the north is forest.',
                          'Enter': (move, 'InCave'), 'North': (move, 'Forest'),
                          'Image': 'cave.png', 'Theme': 'DarkBlack1'},
                'Village': {'Story': 'You are at the village.\n- Talk to the chief.\n- To the east is the forest.', 
                         'Talk': (talk_to_chief, 'Chief'), 'East': (move, 'Forest'),
                         'Image': 'village.png', 'Theme': 'DarkGrey1'},
                'InCastle': {'Story': 'You  step foot through the grand entrance. Gazing aroung the elaborate foyer, your eyes set on the looming shape of a vampire, standing at the top of the staircase.\n\n- Fight\n- Escape',
                        'Fight': (fight, 'Vampire'), 'Escape': (move, 'Castle'),
                        'Image': 'castle.png', 'Theme': 'Reddit'},
                'Vampire': {'Story': 'Excitement ripples throughout your body as you prepare to battle the vampire.\n\n- Fight\n- Escape',
                        'Fight': (fight, 'Vampire'), 'Escape': (move, 'Castle'),
                        'Image': 'castle.png', 'Theme': 'Reddit'},
                'Ocean': {'Story': 'Hot from a long day of travel, you decide to cool down with a quick swim. Wading through the cool water, you feel a solid object buried in the sand.\n\n- Pickup\n- Leave',
                        'Pickup': (pickup_key, 'Coast'), 'Leave': (move, 'Coast'),
                        'Image': 'coast.png', 'Theme': 'LightBrown11'},
                'InCave': {'Story': 'Flaming torch in hand, you work your way through the narrow cave passageway. Eventually, the walls open up into a large chamber, covered in mounds of spider webs.\n\n- Search cave\n- Leave',
                        'Search': (move, 'SearchCave'), 'Leave': (move, 'Cave'),
                        'Image': 'cave.png', 'Theme': 'DarkBlack1'},
                'SearchCave': {'Story': 'Pushing through the thick web, you find the skeletal remains of a body. On the ground next to it lies a slightly rusted sword. \n\n- Pickup\n- Leave',
                        'Pickup': (pickup_sword, 'Cave'), 'Leave': (move, 'Cave'),
                        'Image': 'cave.png', 'Theme': 'DarkBlack1'},
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    return f'[Health={HP.get()}]\n\n'+game_places[game_state]['Story']


def game_play(command_input):
    """
    Runs the game_play

    Args:
        command input string:
    Returns:
        string: the story at the current place, after an action
    """
    global game_state
    story_result = ''
    valid_tokens = TKN.valid_list(command_input)
    if not valid_tokens:
        story_result = 'Can not understand that sorry\n'+show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            event = atoken.capitalize()
            if event in game_place:
                place = game_place[event]
                story_result = place[0](place)  # Run the action
            elif event == 'Inventory':
                story_result = display_inventory(game_place)
            else:
                story_result = f"Can't {event} here\n"+show_current_place()
    return story_result
