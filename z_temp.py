from game_manager import *

# player_instance_name = input("Hello, what is your name? \n>> ")
# player_instance_name = player_instance_name.strip()

player_instance_name = "Tav"

events_list = game_manager.setup_events()

event_current = events_list[2]

player_instance = game_manager.setup_player(player_instance_name)

#####################################################################################################################################################
# Created during entry start
character_string = event_current.characters
character_instance = game_manager.setup_character(character_string)

# Start Combat
turn = 1

continue_combat = "TRUE"

while ( continue_combat == "TRUE" ):
    print("====================================================================")
    if (turn == 1):
        # player attempt to attack character
        game_manager.execute_attack(player_instance, character_instance)
        turn = turn - 1
    else:
        # character attemtps to attack player
        turn = turn + 1
        game_manager.execute_attack(character_instance, player_instance)

    if (int(character_instance.hp) < 0 or (int(player_instance.hp) < 0) ):
        continue_combat = "FALSE"

if ( (int(player_instance.hp) <= 0) ):
    print("You have 0 Hit Points.")

else:
    print("You have defeated the " + character_instance.name + "!")