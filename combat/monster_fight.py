"""This module handles the combat system for the monster fight.

Functions:
    get_boss_health()
    player_attack(weapon)
    boss_attack()
    fight(weapon)

Global Variables:
    _boss_health (int)
"""

# Import modules
import random as RND
import status.health as HP


# Global variables
_boss_health = 15


# Functions
def get_boss_health():
    """Retrieves the boss's health.

    Returns:
        _boss_health (int): The boss's health
    """
    return _boss_health


def player_attack(weapon):
    """Processes the player's attack and damage dealt.

    Parameters:
        weapon (str): The weapon used by the player

    Returns:
        result (str): The result of the player's attack
    """
    global _boss_health

    if weapon == "Sword":
        result = RND.randint(3, 5)
        _boss_health -= result
    elif weapon == "Crystal":
        result = RND.randint(9, 10)
        _boss_health -= result
        return (
            "You pull out the glowing crystal, it begins to glow brighter"
            "and brighter. You throw it at the vampire, it explodes on "
            "impact dealing " + str(result) + " damage."
        )
    else:
        result = RND.randint(1, 2)
        _boss_health -= result

    return (
        "You attack the vampire with your "
        + weapon
        + " dealing "
        + str(result)
        + " damage."
    )


def boss_attack():
    """Processes the boss's attack and damage dealt.

    Returns:
        result (str): The result of the boss's attack
    """

    vampire_attack = RND.randint(1, 5)

    if vampire_attack == 1:
        HP.decrease(4)
        result = (
            "The vampire lunges at you, sinking his fangs into "
            "your neck dealing 4 damage."
        )
    elif vampire_attack == 2 or vampire_attack == 3:
        HP.decrease(2)
        result = (
            "The vampire swings his fist at you, knocking "
            "you to the ground dealing 2 damage."
        )
    else:
        HP.decrease(1)
        result = (
            "The vampire grabs you by the throat, lifting "
            "you off the ground dealing 1 damage."
        )

    return result


def fight(weapon):
    """Processes the player's and boss's attacks.

    Parameters:
        weapon (str): The weapon used by the player

    Returns:
        message (str): The result of the player's and boss's attacks
    """
    # Process attacks
    result_1 = player_attack(weapon)
    result_2 = boss_attack()

    # Return attack messages
    message = result_1 + "\n\n" + result_2
    return message
