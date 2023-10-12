from setup_manager import *

events_list = setup_manager.setup_events()

event_start = 0
event_number_offset = 1

event_current = events_list[event_start]

game_state = "ON"

while(game_state == "ON"):

    print(setup_manager.setup_seperator())
    event_current.show_all()
    valid_input = "FALSE"
    
    while (valid_input == "FALSE"):
        
        event_choice = input(">> ")

        valid_input = event_current.verify_option(event_choice)

        if (valid_input == "TRUE"):
            event_choice_int = int(event_choice)
            event_current = events_list[event_choice_int - event_number_offset]
        else:
            print("Please input a number listed on the options.")
