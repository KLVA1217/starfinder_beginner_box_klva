from game_manager import *

events_list = game_manager.setup_events()

event_start = 0
event_number_offset = 1

event_current = events_list[event_start]

player_instance_name = input("Hello, what is your name? \n>> ")

#player_instance = game_manager.setup_player(player_instance_name)

game_state = "ON"

while(game_state == "ON"):

    print(game_manager.setup_seperator())

    event_has_character = event_current.check_for_character()
    event_has_skill_check = event_current.check_for_skill_check()

    event_explored_condition = event_current.check_for_explored()
    #event_update_equipment = event_current.update_equipment

    event_has_equipment_update = event_current.check_for_update_equipment()

    # print("Current event explored state: " + event_explored_condition)
    # print("Current event update_equipment: " + str(event_update_equipment))

    if event_current.entry_number == "1":
        player_instance = game_manager.setup_player(player_instance_name)

        events_list = ""
        events_list = game_manager.setup_events()
        # Need to create a way to reset the explored status on some events...

    if (event_explored_condition == "FALSE"):
        event_current.explored_true()

    # event_current.show_paragraphs()

    valid_input = "FALSE"

    if event_current.entry_number == "23":
        print("Congrats! You've finished the game. Would you like to exit the game or start a new one?")
        print("To exit the game type press enter.")
        print("To start a new game, input a 1")

        input_string = ">> "
        event_choice = input(input_string)

        while (valid_input == "FALSE"):
            if (event_choice == ""):
                exit
            elif(event_choice != "1"):
                print("Please input a valid response. Either a 1 or press the Enter Key")
            else:
                player_instance = game_manager.setup_player(player_instance_name)
                # Need to implement a way to reset the explored status on some events

    while (valid_input == "FALSE"):
        
        event_current.show_paragraphs()
        
        if (event_explored_condition == "TRUE"):
            event_current = events_list[ int(event_current.option_for_explored)  - event_number_offset]
            break

        elif (event_has_character == "FALSE" and event_has_skill_check == "FALSE"):

            if(event_has_equipment_update == "TRUE"):
                player_instance.update_stat(event_current.update_equipment)

            # print("\n")
            event_current.show_options()
            if(player_instance.healing_serums > 0 ):
                print("Use a healing serum, h")

            input_string = ">> "
            event_choice = input(input_string)

            if(event_choice.strip() == ("h" or "H")): player_instance.healing_serum_activity()

            valid_input = event_current.verify_option(event_choice)

            if (valid_input == "TRUE"):
                event_choice_int = int(event_choice)
                event_current = events_list[event_choice_int - event_number_offset]
            else:
                print("Please input a number listed on the options.\n")

        elif (event_has_character == "TRUE"):
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

        else:
            event_skill_check_string = event_current.skill_check
            skill_check_string_split = event_skill_check_string.split(",")
            skill_check_name = skill_check_string_split[0].strip()

            current_event_skill_check_options = event_current.skill_check_options()

            # print("***DEBUG***")
            # print(current_event_skill_check_options)

            input_string = "Press enter to start a " + skill_check_name + " skill check..."

            event_choice = input(input_string)

            difficulty_class = int(skill_check_string_split[1].strip())

            skill_check_result = game_manager.roll_dice(20)

            print("You rolled a " + str(skill_check_result) +"!")

            current_event_skill_check_options = event_current.skill_check_options()

            if(skill_check_result >= difficulty_class):
                print("You have succeeded!")
                skill_check_success_entry = current_event_skill_check_options[0]
                event_choice_int = int(skill_check_success_entry)

            else:
                print("You have failed...")
                skill_check_failed_entry = current_event_skill_check_options[1]
                event_choice_int = int(skill_check_failed_entry)

            event_current = events_list[event_choice_int - event_number_offset]

            input_string = "Press enter to continue... "
            input(input_string)

            valid_input = "TRUE"