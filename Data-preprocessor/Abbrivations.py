import csv



class Abbrivations:

    def __init__(self, abb):
        self.abb=abb


    def lookup(self):
        try:
            with open("abbrivations.csv", "a", newline="\n")as csv_file:
                    line_reader = csv.reader(csv_file)
                    r1 = csv.get_dialect(self.abb)
                    return r1
        finally:
            csv_file.close()

    def add_abbrivation(self, abb, word):
        with open("abbrivations.csv", "a", newline="\n")as csv_file:
            line_writer = csv.writer(csv_file)
            line_writer.writerow([abb,word])




