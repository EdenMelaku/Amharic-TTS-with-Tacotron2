import csv



class Abbrivations:

    def __init__(self, abb):
        self.abb=abb


    def lookup(self):

        with open('../Dataset/Abbrivations.csv', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if(self.abb == str(row[0])) :
                    return str(row[1])
            return 0


    def add_abbrivation(self, abb, word):
        with open("abbrivations.csv", "a", newline="\n")as csv_file:
            line_writer = csv.writer(csv_file)
            line_writer.writerow([abb,word])

if __name__ == "__main__":

    ab=Abbrivations("ለም/ቤቱ")
    print(ab.lookup())



