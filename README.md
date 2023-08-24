# SDV602-A1-Game

Python game for SDV602 assessment 1. Please read this document before setting up and playing the game. 
Code has been formatted using the pep guide and black formatter.
<br><br>

## Dependancies

- Python V3.11.4
- PySimpleGUI V4.60.5
- PSG-Reskinner V2.3.8
- Colour V0.1.5

These can be installed by running the command `pip install -r requirements.txt` in the terminal.

Note: the black formatter has been used in this project, but it should not be necessary to install.
<br><br>

## Installation

How to run the game:

1. Download the repository and open in VS Code.
2. Download the dependancies (see above).
3. Run the SimpleGame.py script.
   <br><br>

## Gameplay Commands

Gameplay is based of entering keywords. Only the first keyword will be processed each turn.

### Used at any time:

- Inventory

### Used in specific locations (indicated):

- North, south, east, west
- Enter, leave, escape
- Fist, sword, crystal
- Talk, search, pickup
  <br><br>

## Story

<b>Warning, story spoilers ahead.</b>

There are two phases that must be completed in order and items that must be completed in order to successfully complete the game.

### Phase 1 (in any order)

- Visit the village to learn the story
- Collect the key from the coast
- Collect the sword and crystal (optional) from the cave

### Phase 2 (boss fight)

- Enter the castle.
- While the castle can be enter once the key is collected, fighting with no weapons will end in death.
- It is possible to win the fight with just the sword, but not guarenteed.
- Using the crystal then sword will guarentee victory
  <br><br>

## Python Data Types

All of the modules use one or more of the following data types.

#### Tuple 

Tuples store multiple items in a single variable. They are immutable and allow duplicates.
Example: command_manager.py, game_places dictionary, line 295. E.g. (move, "Castle") stores the function that will handle the action and the parameter to be passed in.

#### List

Lists store multiple items in a single variable. They are mutable and allow duplicates.
Example: token_handler, valid_list(), line 42. E.g. Result = [] is appended the valid tokens.

#### Dictionary
Dictionaries store multiple items in a single variable. They are mutable and use unique keys to store values.
Example: command_manager.py, game_places dictionary, line 288. E.g. game_places = {"Forest": {-forest details-}, "Coast": {-coast details-}, etc} stores subdictionaries with information about each game state.

#### Set

Sets store multiple items in a single variable. They are mutable and does not allow duplicates.
Example: contents.py, line 15. E.g. _player_inventory = set() creates an empty set for the inventory.

#### Comprehensions

List Comprehensions are syntax for creating new lists out of existing lists while performing an operator on each item. I have not used any in this game as they were not useful, however one could be done like: new_list = [item for item in old_list if item > 10].

