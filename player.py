class player:
    def __init__(self, name, atk, damage, ac, hp, credits, healing_serums, hampered):
        self.name = name
        self.atk = atk
        self.damage = damage
        self. ac = ac
        self.hp = hp
        self.credits = credits
        self.healing_serums = healing_serums
        self.hampered = hampered

    def update_hp(self, value_int):
        hp_int = int(self.hp)
        hp_int = hp_int + value_int
        hp_string = str(hp_int)
        self.hp = hp_string

    def update_stat(self, update_equipment_string):
        update_equipment_string_split = update_equipment_string.split(",")

        type = update_equipment_string_split[0].strip()
        value = update_equipment_string_split[1].strip()

        # print("DEBUG: ")
        print_debug_string = "\tPlayer Stat Updated: " + type + ", "

        if (type == "weapon"):
            self.damage = value
            value_string = str(self.damage)
        
        elif(type == "credits"):
            self.credits = self.credits + int(value)
            value_string = str(self.credits)

        elif(type == "healing_serum"):
            self.healing_serums = self.healing_serums + int(value)
            value_string = str(self.healing_serums)

        print_debug_string = print_debug_string + value_string
        # print(print_debug_string)

    def healing_serum_activity(self):
        if (self.healing_serums == 0):
            print("You don't have any healing serums...")
            return
        else:
            input_string = ">> "

            while (input_string != "Y" or "y" or "N" or "n"):

                print("You have " + str(self.healing_serums) + "healing serums. Would you like to use one?")
                print("Current HP: " + str(self.hp))
                print("*Note you cannot heal beyond your max HP of 14")
                print("Enter (Y)es or (N)o")

                input_string = ">> "
                player_input = input(input_string)

                if(player_input == "Y" or "y"):
                    print("You use the healing serum.")

                    self.hp = str(int(self.hp) + 8)

                    if(int(self.hp) > 14):
                        self.hp = 14
                    self.healing_serums = self.healing_serums - 1
                    
                    print("New HP: " + str(self.hp))
                    print("Available Healing Serums: " + str(self.healing_serums))
                    return
                else:
                    print("You have chosen not to use the healing serum")
                    return
            
        return

    def show_player_stats(self):
        print("Name: " + self.name)
        print("Attack Bonus: " + str(self.atk))
        print("Damage: " + str(self.damage))
        print("Armor Class: " + str(self.ac))
        print("Hit Points: " + str(self.hp))
        print("Credits: " + str(self.credits))
        print("Healing Serums: " + str(self.healing_serums))
        print("Hampered: " + str(self.hampered))