from event import *
import os 
from player import *
from character import *

class game_manager:

    def setup_seperator():
        size = os.get_terminal_size()
        columns = size[0]

        seperator = ""

        for iterator in range(columns):
            seperator = seperator + "="

        return seperator

    def setup_events():

        file_to_read = "events.txt"

        f = open(file_to_read, "r")

        lines = f.readlines()

        events = []

        paragraphs_current = ""
        options_current = ""
        characters_current = ""
        skill_check_current = ""

        for line in lines:
            line_split = line.split(":")

            name = line_split[0].strip()
            value = line_split[1].strip()

            if(name == "entry_number"):
                if value == "XX":
                    break
                else:
                    entry_number_current = value.strip()

            elif(name == "paragraph"):
                paragraphs_current = paragraphs_current + value.strip() + "|"

            elif(name == "option"):
                options_current = options_current + value.strip() + "|"

            elif(name == "character" and value != "NONE"):
                characters_current = characters_current + value.strip() + "|"

            elif(name == "skill_check" and value != "NONE"):
                skill_check_current = value.strip()

            elif(name == "DONE" and value != "!!"):
                paragraphs_current.strip()
                paragraphs_current = paragraphs_current[:-1]

                options_current.strip()
                options_current = options_current[:-1]

                characters_current.strip()
                characters_current = characters_current[:-1]

                event_current = event(entry_number_current, paragraphs_current, options_current, characters_current, skill_check_current)

                events.append(event_current)

                paragraphs_current = ""
                options_current = ""
                characters_current = ""
                skill_check_current = ""

        return events

    def setup_player(name):
        player_atk = 4
        player_damage = "1d4"
        player_ac = 15
        player_hp = 14
        
        player_instance = player(name, player_atk, player_damage, player_ac, player_hp)

        return player_instance
    
    def setup_character(character_string):
        character_string_split = character_string.split(",")

        character_name = character_string_split[0].strip()
        character_atk = character_string_split[1].strip()
        character_damage = character_string_split[2].strip()
        character_ac = character_string_split[3].strip()
        character_hp = character_string_split[4].strip()

        character_instance = character(character_name, character_atk, character_damage, character_ac, character_hp)

        return character_instance
    
    def roll_dice(dice):

        dice_result = random.randrange(1,dice+1)

        return dice_result
    
    def execute_attack(attacker, defender):
        attacker_attack_roll = game_manager.roll_dice(20) + int(attacker.atk)

        if (attacker_attack_roll >= int(defender.ac) ):

            print(attacker.name + " succesfully hit " + defender.name)

            attacker_damage_list = attacker.damage.split("d")

            number_of_dice = int(attacker_damage_list[0])
            value_damage = int(attacker_damage_list[1])

            player_attack_damage = 0

            for iterator in range(number_of_dice):
                player_attack_damage = player_attack_damage + game_manager.roll_dice(value_damage)

            print(attacker.name + " damaged " + defender.name + " with their weapon for " + str(player_attack_damage) + " damage.")

            player_attack_damage = -player_attack_damage

            defender.update_hp(player_attack_damage)

            print(defender.name + " now has " + defender.hp)

        else:
            print(attacker.name + " failed to hit " + defender.name)
            print(attacker.name + " rolled " + str(attacker_attack_roll))