"""_summary_
    Handles the combat system.
"""

import random as RND
import status.health as HP

_boss_health = 15


def get_boss_health():
    """
    Returns:
        _type_: _description_
    """
    return _boss_health


def player_attack(event):
    """
    Args:
        event (_type_): _description_

    Returns:
        _type_: _description_
    """
    global _boss_health

    if event == 'Sword':
        result = RND.randint(3, 5)
        _boss_health -= result
    elif event == 'Crystal':
        result = RND.randint(9, 10)
        _boss_health -= result
        return "You pull out the glowing crystal, it begins to glow brighter and brighter. You throw it at the vampire, it explodes on impact dealing "+str(result)+" damage."
    else:
        result = RND.randint(1, 2)
        _boss_health -= result

    return "You attack the vampire with your "+event+" dealing "+str(result)+" damage."



def boss_attack():
    """
    Returns:
        _type_: _description_
    """

    vampire_attack = RND.randint(1, 5)

    if vampire_attack == 1:
        HP.reduce(4)
        result = "The vampire lunges at you, sinking his fangs into your neck dealing 4 damage."
    elif vampire_attack == 2 or vampire_attack == 3:
        HP.reduce(2)
        result = "The vampire swings his fist at you, knocking you to the ground dealing 2 damage."
    else:
        HP.reduce(1)
        result = "The vampire grabs you by the throat, lifting you off the ground dealing 1 damage."
    
    return result


def fight(event):
    # event is the weapon
    result_1 = player_attack(event)
    
    result_2 = boss_attack()

    # return attack messages
    return result_1+'\n\n'+result_2

    