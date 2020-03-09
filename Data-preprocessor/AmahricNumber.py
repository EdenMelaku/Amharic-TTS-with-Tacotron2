from re import split




class Amharic_Numbers:
    ones = ['', 'አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ']
    tenth = ['', 'አስራ', 'ሃያ', 'ሰላሳ', 'አርባ', 'ኃምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና']
    higher = ['', '', 'መቶ', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
    num = 0

    def __init__(self, number):
       self.num = number

    def returnOnes(self):
        digits = [int(d) for d in str(self)]
        s = ''
        for d in digits:
            s = s + " " + self.ones[d]

    def returnSubNumbers(self, number):
        digits = [int(d) for d in str(number)]
        s = ''
        if (digits[0] != 0):
            s = s + self.ones[digits[0] - 1] + " " + self.higher[0]
        if (digits[1] != 0):
            if (digits[2] == 0):
                if (digits[1] == 1):
                    return s + " አስር"
                return s + " " + self.tenth[digits[1] - 1]
            return s + " " + self.tenth[digits[1] - 1] + " " + self.ones[digits[2] - 1]

        if (digits[2] != 0):
            s = s + " " + self.ones[digits[2] - 1]

    def returnFullNumber(self):

        digits = [int(d) for d in str(self.num)]
        rev = digits.reverse()
        s = '';
        i = digits.__len__()
        j = 0
        while (rev):
            s = self.returnFullNumber() + s

    def num_to_word(self):
        ones = ['', 'አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ']
        tenth = ['', 'አስራ', 'ሃያ', 'ሰላሳ', 'አርባ', 'ኃምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና']
        higher = ['', '', 'መቶ', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
        digits = [int(d) for d in str(self.num)]
        s = '';
        x = 0;
        leng = len(digits) - 1
       # print("length" + str(leng))
        i = len(digits) / 3
        while (x <= leng):
            #print(x)
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

            x = x + 1

        # print(s)
        return s

    def convert_year(self):

        if (len(str(self.num))) < 4:
            return self.num_to_word(self.num)
        else :
            n1=Amharic_Numbers(str(self.num)[0:2])
            n2=Amharic_Numbers(str(self.num)[2:4])
            return n1.num_to_word() +" "+n2.num_to_word()

if __name__ == "__main__":
        num = 231040
        units = ['', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
        nuu = "1236831200149"
        nu = "10105090000"
        n = "60,000,678"
        commas = []
        unit = 0
        s = ""
        obj = Amharic_Numbers(num)
        if (len(nu) % 3 != 0):
            unit += 1 + ((len(nu) - (len(nu) % 3)) // 3)
            i = len(nu) % 3
            n1=nu[0:len(nu) % 3]
            objj=Amharic_Numbers(n1)
            s = objj.num_to_word()
            s+= " " + units[unit - 1]
            unit -= 1
        else:
            unit = len(nu) // 3
            i = 0

        for x in range(unit):
            ob=Amharic_Numbers(nu[i:i + 3])
            if (ob.num_to_word() != " "):
                s = s + " " + ob.num_to_word() + " " + units[unit - 1]
            unit -= 1
            i += 3

        print(s)
        print("###########")
        obj1=Amharic_Numbers(1997)
        print(obj1.convert_year())
