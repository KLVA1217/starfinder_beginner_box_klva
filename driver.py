from game_manager import *

events_list = game_manager.setup_events()

event_start = 0
event_number_offset = 1

event_current = events_list[event_start]

player_instance_name = input("Hello, what is your name? \n>> ")

player_instance = game_manager.setup_player(player_instance_name)

game_state = "ON"

while(game_state == "ON"):

    print(game_manager.setup_seperator())

    event_has_character = event_current.check_for_character()

    event_current.show_paragraphs()

    valid_input = "FALSE"
    
    while (valid_input == "FALSE"):
        
        if (event_has_character == "FALSE"):
            print("\n")
            event_current.show_options()

            input_string = ">> "
            event_choice = input(input_string)

            valid_input = event_current.verify_option(event_choice)

            if (valid_input == "TRUE"):
                event_choice_int = int(event_choice)
                event_current = events_list[event_choice_int - event_number_offset]
            else:
                print("Please input a number listed on the options.")

        else:
            input_string = "Press enter to start combat... "
            event_choice = input(input_string)

            character_string = event_current.characters
            character_instance = game_manager.setup_character(character_string)

            turn = 1
            continue_combat = "TRUE"

            while ( continue_combat == "TRUE" ):
                print("====================================================================")
                if (turn == 1):
                    game_manager.execute_attack(player_instance, character_instance)
                    turn = turn - 1
                else:
                    turn = turn + 1
                    game_manager.execute_attack(character_instance, player_instance)

                if (int(character_instance.hp) < 0 or (int(player_instance.hp) < 0) ):
                    continue_combat = "FALSE"

            current_event_combat_options = event_current.combat_options()

            if ( (int(character_instance.hp) <= 0) ):
                print("You have defeated the " + character_instance.name + "!")
                combat_victory_entry = current_event_combat_options[0]
                event_choice_int = int(combat_victory_entry)
                
            else:
                print("You have 0 Hit Points.")
                combat_defeat_entry = current_event_combat_options[1]
                event_choice_int = int(combat_defeat_entry)

            event_current = events_list[event_choice_int - event_number_offset]

            input_string = "Press enter to continue... "
            input(input_string)

            valid_input = "TRUE"