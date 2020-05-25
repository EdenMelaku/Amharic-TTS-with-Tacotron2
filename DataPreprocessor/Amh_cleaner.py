from re import split, match
from .AmharicNumber import convert_year, convert_decimals, convert_number
from .Abbrivations import lookup

class Cleaner:
    def __init__(self, text):
        self.text = text

    def clean(self):

        words = split(" ", self.text)
        text = ""
        i = 0
        for word in words:

            if any(map(str.isdigit, word)):


                if i<(len(words)-1):
                   if (words[i + 1] == "ዓ.ም" or words[i + 1] == "ዓ/ም" or words[i + 1] == "ዓ.ዓ" or words[i + 1] == "ዓ/ዓ"):
                      text = text + " " + convert_year(word)

                if (str(word).__contains__('.')):
                   text += " " + convert_decimals(word)
                else:
                   text = text + " " + convert_number(word)

            elif word.__contains__("/") or word.__contains__("."):

                text = text + " " + str(lookup(word))
            else:
                text += " " + word
            i += 1
        return text
