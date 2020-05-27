from re import split

ones = ['ዜሮ', 'አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ']
tenth = ['', 'አስራ', 'ሃያ', 'ሰላሳ', 'አርባ', 'ኃምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና']
higher = ['', '', 'መቶ', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']


def returnOnes( num):
    digits = checkDigit(num)
    s = ''
    for d in digits:
        s = s + " " + ones[d]
    return s


def returnSubNumbers(number):
    digits = checkDigit(number)
    s = ''
    if (digits[0] != 0):
        s = s + ones[digits[0] - 1] + " " + higher[0]
    if (digits[1] != 0):
        if (digits[2] == 0):
            if (digits[1] == 1):
                return s + " አስር"
            return s + " " + tenth[digits[1] - 1]
        return s + " " + tenth[digits[1] - 1] + " " + ones[digits[2] - 1]

    if (digits[2] != 0):
        s = s + " " + ones[digits[2] - 1]


def returnFullNumber(num):
    digits = checkDigit(num)
    rev = digits.reverse()
    s = '';
    i = digits.__len__()
    j = 0
    while (rev):
        s = returnFullNumber() + s
def checkDigit(num):
    dig = [d for d in str(num)]
    digits = []
    for d in dig:
        if (d.isdigit()):
            digits.append(int(d))
    return digits

def num_to_word(num):

    digits=checkDigit(num)
    #print(num)
    #print(digits)
    s = ''
    x = 0
    leng = len(digits) - 1
    # print("length" + str(leng))
    i = len(digits) / 3
    while (x <= leng):
        # print(x)
        if (x == 1):
            if (s == ''):
                if (digits[leng - 1] == 1):
                    s = "አስር"
                else:
                    s = tenth[digits[leng - x]] + " " + s
            else:
                s = tenth[digits[leng - x]] + " " + s
        else:
            re = ones[digits[leng - x]]
            if (digits[leng - x] != 0):
                # print(ones[digits[leng - x]])
                s = re + " " + higher[x] + " " + s
            # printdi(s)

        x = x + 1

    # print(s)
    return s


def convert_year(num):
    if (len(str(num))) < 4:
        return num_to_word(num)
    elif str(num).startswith("1"):
        return num_to_word(num[0:2]) + " " + num_to_word(num[2:4])
    else:
        return num_to_word(num)


def convert_decimals(num):

    split_num = checkDigit(str(num).split('.'))
    int_part = int(split_num[0])
    decimal_part = split_num[1]
    dec=""
    if(str(decimal_part).startswith('0')):
        dec=" ዜሮ "
    decimal_part = int(split_num[1])
    text = num_to_word(int_part) + " " + "ነጥብ" + dec+returnOnes(decimal_part)
    return text


def convert_number(num):
    unit = 0
    units = ['', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
    num = num.replace(',', '')
    s=""
    if (len(num) % 3 != 0):
        unit += 1 + ((len(num) - (len(num) % 3)) // 3)
        i = len(num) % 3
        n1 = num[0:len(num) % 3]
        s = num_to_word(n1)
        s += units[unit - 1]
        unit -= 1
    else:
        unit = len(num) // 3
        i = 0

    for x in range(unit):
        if (num_to_word(num[i:i + 3]) != " "):
            s = s + " " + num_to_word(num[i:i + 3]) + " " + units[unit - 1]
        unit -= 1
        i += 3
    return s
