class event:

    def __init__(self, entry_number, paragraphs, options, characters, skill_check):
        self.entry_number = entry_number
        self.paragraphs = paragraphs
        self.options = options
        self.characters = characters
        self.skill_check = skill_check

    def show_paragraphs(self):
        paragraph_list = self.paragraphs.split("|")

        for paragraph in paragraph_list:
            print(paragraph)

    def show_options(self):
        options_list = self.options.split("|")

        for option in options_list:
            print(option)

    def verify_option(self, number_to_verify):
        number_to_verify.strip()
        options_list = self.options.split("|")

        for option in options_list:
            option.strip()
            option_split = option.split(",")

            # text = option_split[0].strip()
            number = option_split[1].strip()

            if (number == number_to_verify):
                return "TRUE"
            
        return "FALSE"
    
    def check_for_character(self):
        if (self.characters == ""):
            return "FALSE"
        else:
            return "TRUE"
        
    def check_for_skill_check(self):
        if (self.skill_check == ""):
            return "FALSE"
        else:
            return "TRUE"

    def show_all(self):
        self.show_paragraphs()
        print("\n")
        self.show_options()

    def combat_options(self):
        combat_options_array = []
        options_list = self.options.split("|")

        for option in options_list:
            option.strip()
            option_split = option.split(",")

            number = option_split[1].strip()

            combat_options_array.append(number)

        return combat_options_array
    
    def skill_check_options(self):
        skill_check_options_array = []
        options_list = self.options.split("|")

        for option in options_list:
            option.strip()
            option_split = option.split(",")

            number = option_split[1].strip()

            skill_check_options_array.append(number)

        return skill_check_options_array