import csv



class Abbrivations:

    def __init__(self, abb):
        self.abb=abb


    def lookup(self):
        try:
            csv_file=csv.reader(open("Abbrivations.csv", "rb"), delimiter=",")
            for row in csv_file:
                if(self.abb == row[0]) :
                    return row[1]
            return 0
        finally:
            csv_file.close()

    def add_abbrivation(self, abb, word):
        with open("abbrivations.csv", "a", newline="\n")as csv_file:
            line_writer = csv.writer(csv_file)
            line_writer.writerow([abb,word])




