import argparse
import csv
import re

filename_initial = "HB"
count = 0


def generate_name():
    global filename_initial, count
    number = ""
    for i in range(5 - len(count)):
        number = number + count
        count += 1
        return filename_initial + "_" + number


def preprocess_data(filename):
    try:
        with open(filename, "rb") as file:
            for cnt, line, in enumerate(file):
                append_csv(line)

    finally:
        file.close()


def clean_english_letters(line):
    return re.sub(r"[a-zA-Z]", "", line)


def clean_Line(line):
    punc_marks = ",?።፣፤፥፦()[]{}/\"\'!$+-"
    for char in punc_marks:
        line = line.replace(char, "")
    return line


def append_csv(line):
    name = generate_name().encode()
    line = clean_english_letters(line).encode()
    clean_line = clean_Line(line).encode()
    with open("metadata.csv", "wb")as csv_file:
        line_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        line_writer.write_row([name, line, clean_line])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fileLocation", help="enter filename")
    args = parser.parse_args()
    filename = args.fileLocation
    print(filename)
    # csv_file=open("metadata.csv","wb")
    preprocess_data(filename)



