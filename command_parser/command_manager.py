"""This module contains the game commands, game state and main gameplay.

Functions:
    move(game_place, extra='')
    pickup_key(game_place)
    pickup_sword(game_place)
    pickup_crystal(game_place)
    enter_castle(game_place)
    talk_to_chief(game_place)
    display_inventory()
    prepFight(event)
    display_combat_actions()
    fight(event)
    show_current_place()
    game_play(command_input)
    
Global Variables:
    game_state (str)
    game_places (dict)
"""

# Import typing
import command_parser.token_handler as TKN
import inventory.contents as INV
import status.health as HP
import combat.monster_fight as FGT


# Game commands
def move(game_place, extra=""):
    """Moves the player to a new location and returns the new story.

    Parameters:
        game_place (tuple): contains (action function, new state)
        extra (str): any extra text to add to the story

    Returns:
        story_result (str): the story at the new location
    """
    global game_state

    game_state = game_place

    story_result = extra + show_current_place()
    return story_result


def pickup_key(game_place):
    """Adds key to inventory and removes it from the coast.

    Parameters:
        game_place (str): contains new state name

    Returns:
        move (function): new location and extra text
    """
    # Add key to inventory
    INV.collect_item("key")

    # Remove key from coast
    game_places["Ocean"].pop("Pickup")
    game_places["Ocean"]["Story"] = (
        "Enjoying the refreshing cool of the water, you enjoy a quick "
        "swim before heading back to shore.\n\n- Leave"
    )

    return move(game_place, "Picked up key.\n\n")


def pickup_sword(game_place):
    """Adds sword to inventory, removes it from the cave and adds
        crystal to the cave.

    Parameters:
        game_place (str): contains new state name

    Returns:
        move (function): new location and extra text
    """
    INV.collect_item("sword")

    # Change pickup to crystal
    game_places["SearchCave"]["Pickup"] = [pickup_crystal, "InCave"]

    # Update story
    game_places["SearchCave"]["Story"] = (
        "Searching through the cave again, you stumble over something "
        "sticking out of the ground. Uncovering it from the years of dirt "
        "and grime, find a glowing crystal.\n\n- Pickup\n- Leave"
    )
    game_places["InCave"]["Story"] = (
        "You stand at the entranceway to the large chamber, torchlight "
        "flickering over the walls.\n\n- Search cave\n- Leave"
    )

    return move(game_place, "Picked up sword.\n\n")


def pickup_crystal(game_place):
    """Adds crystal to inventory, removes it from the cave and
        changes story text.

    Parameters:
        game_place (str): contains new state name

    Returns:
        move (function): new location and extra text
    """
    INV.collect_item("crystal")

    # Remove pickup from cave
    game_places["SearchCave"].pop("Pickup")
    game_places["SearchCave"]["Story"] = (
        "Curious if there are any other secrets in the cave, you search "
        "around the chamber but find nothing.\n\n- Leave"
    )

    return move(game_place, "Picked up crystal.\n\n")


def enter_castle(game_place):
    """Enter the castle if the player has the key.

    Parameters:
        game_place (str): contains new state name

    Returns:
        result (str): move function or show current story function
    """
    result = ""
    if INV.has_item("key"):
        result = move(game_place)
    else:
        result = "The door is locked.\n\n" + show_current_place()
    return result


def talk_to_chief(game_place):
    """Talk to the chief.

    Parameters:
        game_place (str): contains new state name

    Returns:
        result (str): chief's message and current story
    """
    result = (
        "Adventurer, please help us. An evil vampire has been attacking our "
        "village. The vampire lives in an old castle up north.\n\n"
        + show_current_place()
    )
    return result


def display_inventory():
    """Displays the player's inventory.

    Returns:
        result (str): the player's inventory and current story
    """
    result = ""
    result = INV.display_inventory() + "\n" + show_current_place()
    return result


def prepFight(event):
    """Adds correct actions to the boss fight state, updates the story
        actions and moves to the boss state.

    Parameters:
        event (tuple): contains (action function, new state)

    Returns:
        story_result (str): the story at the boss state
    """
    # Add correct actions depending on inventory
    if INV.has_item("sword"):
        game_places["Boss"]["Sword"] = (fight, "Sword")
    if INV.has_item("crystal"):
        game_places["Boss"]["Crystal"] = (fight, "Crystal")

    # Update story to include actions
    display_combat_actions()

    # Move and display story
    story_result = move((move, "Boss"))
    return story_result


def display_combat_actions():
    """Updates story actions for the boss state to match the inventory."""
    global game_places

    result = ""
    # Add correct actions depending on inventory
    if INV.has_item("crystal"):
        result += "- Crystal\n"
    if INV.has_item("sword"):
        result += "- Sword\n"
    # Fist and escape are always options
    result += "- Fist\n"
    result += "- Escape"
    # Check if combat started
    message = ""
    if FGT.get_boss_health() == 15:
        message += "The vampire grins at you menacingly.\n\n"
    message += result
    game_places["Boss"]["Story"] = message


def fight(event):
    """Performs the combat action and updates the story.

    Parameters:
        event (tuple): contains (action function, new state)

    Returns:
        message (str): the result of the combat
    """
    # Perform combat
    result = FGT.fight(event[1])

    # Remove crystal if used
    if event[1] == "Crystal":
        INV.remove_item("crystal")
        game_places["Boss"].pop("Crystal")
    # Regenerate story actions
    display_combat_actions()

    # Check if player or boss is dead
    if HP.get() <= 0:
        message = move(("Move", "Dead"))
    elif FGT.get_boss_health() <= 0:
        message = move(("Move", "Win"))
    else:
        message = result + "\n\n" + show_current_place()

    return message


def show_current_place():
    """Gets the story at the game_state place.

    Returns:
        fstring (str): current HP and the story at the current place
    """
    global game_state
    return f"[Health={HP.get()}]\n\n" + game_places[game_state]["Story"]


def game_play(command_input):
    """Runs the main game_play.

    Parameters:
        command_input (str): the command entered by the player
    Returns:
        story_result (str): calls token validation and returns the story at
                            the new location or other messages
    """
    global game_state
    story_result = ""
    valid_tokens = TKN.valid_list(command_input)
    if not valid_tokens:
        story_result = "Invalid command.\n\n" + show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            event = atoken.capitalize()
            # If event token in current location options
            if event in game_place:
                place = game_place[
                    event
                ]  # Place = action key: (action function, new state)
                story_result = place[0](place[1])  # Call action function with place
            elif event == "Inventory":
                story_result = display_inventory()
            else:
                story_result = (
                    f"Can't perform action {event} here\n\n" + show_current_place()
                )
    return story_result


# Game variables
game_state = "Forest"
# Format is:
# {state: {story: str, action/direction: (action function, new state), etc}}
game_places = {
    "Forest": {
        "Story": (
            "You are in the forest.\n- To the north is a castle\n"
            "- To the east is the coast.\n- To the south is a cave.\n"
            "- To the west is a village."
        ),
        "North": (move, "Castle"),
        "East": (move, "Coast"),
        "South": (move, "Cave"),
        "West": (move, "Village"),
        "Image": "forest.png",
        "Theme": "DarkGreen",
    },
    "Castle": {
        "Story": (
            "You are at the castle.\n- Enter the castle.\n- To the south is forest."
        ),
        "Enter": (enter_castle, "InCastle"),
        "South": (move, "Forest"),
        "Image": "castle.png",
        "Theme": "Reddit",
    },
    "Coast": {
        "Story": (
            "You are at the coast.\n- Enter the water.\n" "- To the west is the forest."
        ),
        "Enter": (move, "Ocean"),
        "West": (move, "Forest"),
        "Image": "coast.png",
        "Theme": "LightBrown11",
    },
    "Cave": {
        "Story": (
            "You are at the cave.\n- Enter the cave.\n" "- To the north is forest."
        ),
        "Enter": (move, "InCave"),
        "North": (move, "Forest"),
        "Image": "cave.png",
        "Theme": "DarkGrey7",
    },
    "Village": {
        "Story": (
            "You are at the village.\n- Talk to the chief.\n"
            "- To the east is the forest."
        ),
        "Talk": (talk_to_chief, "Chief"),
        "East": (move, "Forest"),
        "Image": "village.png",
        "Theme": "DarkGrey1",
    },
    "InCastle": {
        "Story": "You step foot through the grand entrance. Gazing aroung "
        "the elaborate foyer, your eyes set on the looming shape of a "
        "vampire, standing at the top of the staircase.\n\n- Fight\n- Escape",
        "Fight": (prepFight, "Boss"),
        "Escape": (move, "Castle"),
        "Image": "castle.png",
        "Theme": "Reddit",
    },
    "Boss": {
        "Story": "The vampire grins at you menacingly.",
        "Fist": (fight, "Fist"),
        "Escape": (move, "Castle"),
        "Image": "vampire.png",
        "Theme": "DarkBrown4",
    },
    "Ocean": {
        "Story": "Hot from a long day of travel, you decide to cool down "
        "with a quick swim. Wading through the cool water, you feel a solid "
        "object buried in the sand.\n\n- Pickup\n- Leave",
        "Pickup": (pickup_key, "Ocean"),
        "Leave": (move, "Coast"),
        "Image": "coast.png",
        "Theme": "DarkTeal12",
    },
    "InCave": {
        "Story": (
            "Flaming torch in hand, you work your way through the narrow "
            "cave passageway. Eventually, the walls open up into a large "
            "chamber, covered in mounds of spider webs.\n\n- Search cave"
            "\n- Leave"
        ),
        "Search": (move, "SearchCave"),
        "Leave": (move, "Cave"),
        "Image": "cave.png",
        "Theme": "DarkBlack1",
    },
    "SearchCave": {
        "Story": (
            "Pushing through the thick web, you find the skeletal remains of "
            "a body. On the ground next to it lies a slightly rusted sword."
            "\n\n- Pickup\n- Leave"
        ),
        "Pickup": (pickup_sword, "InCave"),
        "Leave": (move, "InCave"),
        "Image": "cave.png",
        "Theme": "DarkBlack1",
    },
    "Dead": {
        "Story": (
            "You were not strong enough to defeat the vampire and died. The "
            "vampire continued to terrorise the villagers. The village was "
            "eventually abandoned, and the vampire continued to live in the "
            "castle for the rest of his days.\n\nGAME OVER"
        ),
        "Image": "dead.png",
        "Theme": "DarkGrey1",
    },
    "Win": {
        "Story": (
            "You have defeated the vampire. The villagers are safe once "
            "again. You are a hero!\n\nGAME OVER"
        ),
        "Image": "castle.png",
        "Theme": "Reddit",
    },
}


if __name__ == "__main__":
    # Assertion tests
    assert game_play("talk") == (
        "Adventurer, please help us. An evil vampire has been attacking our "
        "village. The vampire lives in an old castle up north.\n\n"
        "[Health=10]\n\nYou are at the village.\n- Talk to the chief.\n"
        "- To the east is the forest."
    )
    assert show_current_place() == "Forest"

