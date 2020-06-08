import csv
import os

def lookup(abb):
    abb = abb.replace(".", "/")
    #print(os.getcwd())
    os.chdir("../text")
    with open('Abbrivations.csv', encoding='utf-16') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (abb == str(row[0])):
                return str(row[1])
        return abb


def add_abbrivation( abb, word):
    with open("abbrivations.csv", "a", newline="\n") as csv_file:
        line_writer = csv.writer(csv_file)
        line_writer.writerow([abb, word])
