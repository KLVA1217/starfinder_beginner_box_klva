class event:

    def __init__(self, entry_number, paragraphs, options):
        self.entry_number = entry_number
        self.paragraphs = paragraphs
        self.options = options

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

    def show_all(self):
        self.show_paragraphs()
        print("\n")
        self.show_options()