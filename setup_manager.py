from event import *
import os 

class setup_manager:

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

            elif(name == "option" and value != "!!"):
                options_current = options_current + value.strip() + "|"

            elif(name == "DONE" and value != "!!"):
                paragraphs_current.strip()
                paragraphs_current = paragraphs_current[:-1]

                options_current.strip()
                options_current = options_current[:-1]
                event_current = event(entry_number_current,paragraphs_current, options_current)

                events.append(event_current)

                paragraphs_current = ""
                options_current = ""

        return events