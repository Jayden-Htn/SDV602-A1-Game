""" 
The main module of the game.  This module will be responsible for the game loop and the game window.
"""
import PySimpleGUI as PSG
import command_parser.command_manager as CMD
import psg_reskinner as RSKN


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    PSG.theme("DarkGreen")  # please make your windows
    prompt_input = [
        PSG.Text("Enter your command", font="Any 14"),
        PSG.Input(key="-IN-", size=(20, 1), font="Any 14", do_not_clear=False),
    ]
    buttons = [PSG.Button("Enter", bind_return_key=True), PSG.Button("Exit")]
    command_col = PSG.Column([prompt_input, buttons], element_justification="r")
    layout = [
        [
            PSG.Image(r"images/forest.png", size=(300, 300), key="-IMG-"),
            PSG.Text(
                CMD.show_current_place(), size=(39, 12), font="Any 12", key="-OUTPUT-"
            ),
        ],
        [command_col],
    ]  # size is the width and height of the story text box

    return PSG.Window("Adventure Game", layout, size=(700, 400))


if __name__ == "__main__":
    window = make_a_window()

    while True:
        event, values = window.read()
        if event == "Enter":
            # send the command to the command manager
            current_story = CMD.game_play(values["-IN-"].lower())
            # update the story text box
            window["-OUTPUT-"].update(current_story)
            # update the image
            window["-IMG-"].update(
                r"images/" + CMD.game_places[CMD.game_state]["Image"], size=(300, 300)
            )
            # update background with PSG reskinner
            new_theme = CMD.game_places[CMD.game_state]["Theme"]
            RSKN.animated_reskin(
                window=window,
                new_theme=new_theme,
                theme_function=PSG.theme,
                lf_table=PSG.LOOK_AND_FEEL_TABLE,
                duration=800,
            )
            pass
        elif event == "Exit" or event is None or event == PSG.WIN_CLOSED:
            break  # out of loop
        else:
            pass

    window.close()
