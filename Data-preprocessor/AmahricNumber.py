from re import split


class Amharic_Numbers:
    ones=['','አንድ','ሁለት','ሶስት','አራት','አምስት','ስድስት','ሰባት','ስምንት','ዘጠኝ']
    tenth=['','አስራ','ሃያ','ሰላሳ','አርባ','ኃምሳ','ስልሳ','ሰባ','ሰማንያ','ዘጠና']
    higher=['','','መቶ','ሺህ','ሚሊዮን','ቢሊዮን','ትሪሊዮን','ኳድሪሊዮን']
    num=0
    def __init__(self):
        num=self;

    def returnOnes(self):
        digits=[int(d) for d in str(self)]
        s='';
        for d in digits:
            s=s+" "+self.ones[d];
    def returnSubNumbers(self,number):
        digits=[int(d) for d in str(number)]
        s=''
        if(digits[0]!=0):
            s=s+self.ones[digits[0]-1]+" "+self.higher[0]
        if(digits[1]!=0):
            if(digits[2]==0):
                if(digits[1]==1):
                    return s+" አስር"
                return s+" "+self.tenth[digits[1]-1]
            return s+" "+self.tenth[digits[1]-1]+" "+self.ones[digits[2]-1]

        if(digits[2]!=0):
                s=s+" "+self.ones[digits[2]-1]


    def returnFullNumber(self):

        digits=[int(d) for d in str(self.num)]
        rev=digits.reverse()
        s='';
        i=digits.__len__()
        j=0
        while(rev):
        
           s= self.returnFullNumber() + s


    def num_to_word(self):
        ones = ['', 'አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ']
        tenth = ['', 'አስራ', 'ሃያ', 'ሰላሳ', 'አርባ', 'ኃምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና']
        higher = ['', '', 'መቶ', 'ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
        digits=[int(d) for d in str(self)]
        s='';
        x=0;
        leng=len(digits)-1
        print("length"+str(leng))
        i=len(digits)/3
        while(x<=leng) :
            print(x)
            if(x==1):
                if(s==''):
                    if (digits[leng-1] == 1): s="አስር"
                    else:
                     s=tenth[digits[leng-x]]+" "+s
                else:
                    s = tenth[digits[leng - x]] + " " + s
            else:
               re=ones[digits[leng-x]]
               if(digits[leng-x]!=0):
                   print(ones[digits[leng-x]])
                   s=re+" "+higher[x]+" "+s

            x=x+1

       # print(s)
        return s

    if __name__=="__main__":
        num=231040
        units=['','ሺህ', 'ሚሊዮን', 'ቢሊዮን', 'ትሪሊዮን', 'ኳድሪሊዮን']
        nu="1236831200149"
        
        #num_to_word(num)

        commas=[]
        unit=0
        #commas=commas.append(0,len(nu)%3)
        #print (nu[0:len(nu)%3])
        s=""
        if(len(nu)%3!=0):
         unit+=1+((len(nu)-(len(nu)%3))//3)
         i=len(nu)%3
         s=num_to_word(nu[0:len(nu)%3]) +" "+ units[unit-1]
         unit-=1
        else:
            unit=len(nu)//3
            i=0

        for x in range(unit):
            if(num_to_word(nu[i:i+3])!=" "):
             s = s+" "+num_to_word(nu[i:i+3]) + " "+units[unit - 1]
            unit-=1
            i+=3

        print(s)











