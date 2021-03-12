'''
one of the limitations of this model is that it cannot read abbriviations or a single alphabetic character along or separately
so i am just gonna try giving every alphabet letter a corresponding word. eg B--> bee
'''

'''
besides the above limitation the model cannot generate sentences that are longer than 11seconds when read, so approximately the model can read approximately 20 words with in 11 sec.
we will do a number of steps to segment a given article in several steps

step 1 - split an article in to a number of sentences by using "." or period, in english language a sentence ends by a dot.
step 2- we will get a number of sentences by aoolying step one, if there is any sentence longer than 20 sec then we will apply step 2 which is 
        separating sentences by comma "," , only applies if a comma exists in the sentence.
step 3- is sentntence is not reduced in to a number of short sentence segments by step 2 then we will apply step 3 which is 
        separating a sentence if there exists a conjuctive word in it , we apply the splitting consicutively in the following order
        and, that, but, or, as, if, when, than, because, while, where, after, so, though, since, until, whether, before, although, nor, like, once, unless, now, except

'''
import math
from text.cleaners import collapse_whitespace

letters = ['A.', 'bee', 'see', 'dee', 'ie', 'ef', 'ji', 'ach', 'ay', 'jay', 'kei', 'el', 'em', 'en', 'ow', 'pee', 'kiw',
           'are', 'aiS', 'tea', 'you', 'vee', 'double you', 'eks', 'waai.', 'zed']


def generateSegemnts(text):
    # sentences=text.split(".")
    sentenceList = []

    for s in text:
        # print("set--- "+s)
        queue = []
        if (len(s.split(" ")) > 19):
            split_by_comma = s.split(",")
            for i in split_by_comma:
                if (len(i.split(" ")) > 19):
                    splited_by_conj = split_by_conjuction(i.split(" ")).split("*")
                    for sent in splited_by_conj:
                        if (len(sent.split(" ")) > 19):
                            splited_by_comma = splitt_by_word_count(sent.split(" "))
                            sentenceList.extend(splited_by_comma.split("*"))
                        else:
                            sentenceList.append(sent)

                else:
                    sentenceList.append(i)
        else:
            sentenceList.append(s)

    return sentenceList

def generate_by_psbd(filename):
    from text.cleaners import collapse_whitespace
    import pysbd
    sentenceList = []
    seg = pysbd.Segmenter(language="am", clean=False)
    with open(filename, "r",encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line= line.replace('—', ' ')
            line= line.replace('”', ' ')
            line= line.replace('“', ' ')
            line= line.replace('"', " ")
            line=collapse_whitespace(line)
            sentences=seg.segment(line)
            sentenceList.extend(sentences)

    validated_sentenceList=[]
    for l in sentenceList:
        leng=len(l.split(" "))

        if(leng>80):
            print(leng)
            validated_sentenceList.extend(MaxDecoder_step_fix(l))
        else:
            validated_sentenceList.append(l)

    return validated_sentenceList


def generateSegemnts_from_file(fileName):
    from text.cleaners import collapse_whitespace
    sentenceList = []
    with open(fileName, "r",encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line=collapse_whitespace(line)
            sentences = str(line).split(". ")

            for sentence in sentences:
                if (len(sentence.split(" ")) > 19):
                    split_by_comma = sentence.split(",")
                    for i in split_by_comma:
                        if (len(i.split(" ")) > 19):
                            splited_by_conj = split_by_conjuction(i.split(" ")).split("*")
                            for sent in splited_by_conj:
                                if (len(sent.split(" ")) > 19):
                                    splited_by_WC = splitt_by_word_count(sent.split(" "))
                                    splited_by_WC=collapse_whitespace(splited_by_WC)
                                    sentenceList.extend(splited_by_WC.split("*"))
                                    #print(":::::::::::::::::::::::::Word Count::::::::::::::::::::::::::::::::::::::::::::::")
                                    #print(str(splited_by_WC.split("*")))
                                else:
                                    sentenceList.append(collapse_whitespace(sent))
                                    #print("::::::::::::::::::::conjuction:::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    #print(sent)
                        else:
                            sentenceList.append(collapse_whitespace(i))
                            #print("::::::::::::::::::::::comma::::::::::::::::::::::::::::::::::::::::::::")
                            #print(i)
                else:
                    sentenceList.append(collapse_whitespace(sentence))
                    #print("::::::::::::::::::::::period:::::::::::::::::::::::::::::::::::::::::::::::")
                    #print(sentence)

    return sentenceList

def MaxDecoder_step_fix(segment):
    #is sentence is too long this function will be called
    if ("፡፡" in segment):
       validated = segment.split("፡፡")
    elif ("፤" in segment):
        validated=segment.split("፤")
    else:
        Splited_by_Conj=split_by_conjuction(segment)
        if(Splited_by_Conj==False):validated=splitt_by_word_count(segment)
        else:validated=Splited_by_Conj
    final_Validated=[]

    for seg in validated:
        if(len(seg.split(" "))>50):
            final_Validated.extend(splitt_by_word_count(seg))
        else:
            final_Validated.append(seg)

    return final_Validated




def validate_generated_segments(segments):
    validated = []

    j=0
    cou=0
    while(j<len(segments)):
      segments[j]=segments[j].replace('—', ' ')
      segments[j]=segments[j].replace('”', ' ')
      segments[j]=segments[j].replace('“', ' ')
      segments[j]=segments[j].replace('"', " ")
      segments[j]= " ".join(segments[j].split())

      n_words=len(segments[j].split(" "))
      #print("/######################" + segments[j] + "/////////////////////////////////////")
      if(n_words<4):
         #print("////////////////////////"+segments[j]+"/////////////////////////////////////")
         #print(segments[j])
         if(len(validated)==0):
            if(n_words+len(segments[j+1].split(" "))<19):
                nw=segments[j]+ ", "+segments[j+1]+"."
                cou+=1
                seg = splitt_by_word_count(nw.split(" "))

                validated.extend(seg.split("*"))
                j+=2
                #print("---------------AAA----------------------")
                #print(seg)
                #print("-------------------------------------")
            else:
                nw = segments[j] + ", "+segments[j + 1]
                cou+=1
                seg= splitt_by_word_count(nw.split(" "))
                validated.extend(seg.split("*"))
                j+=2
                #print("----------------BBB---------------------")
                #print(seg)
                #print("-------------------------------------")
         else:
             #sentence=validated[val]
             sentence=validated.pop()
             nw =  sentence+ ", "+segments[j]+"."
             cou+=1
             #print("-----------------ToDO--------------------")
             #print(nw)
             #print("-------------CCC------------------------")

             if(len(nw.split(" "))>19):
               seg = splitt_by_word_count(nw.split(" "))
               validated.extend(seg.split("*"))
               #print(seg)
               #print("------------CDCD-------------------------")

               j += 1
             else:
                 validated.append(nw)
                 #print(nw)
                 j+=1
                 #print("-------------DCDDDDDD------------------------")

      else:

          validated.append(segments[j])

          j+=1
          #print("-----============-----NOTTTTToDO B/C "+str(n_words)+"----------===========----------")

          #print("======="+validated[len(validated)-1]+"=======")
    #print("======================="+str(cou)+"======================================")
    finalValidated=[]
    for v in validated:
        v= " ".join(v.split())
        v+="."
        finalValidated.append(v)
    return validated




def splitt_by_word_count(text):
    text=text.split(" ")
    newtex = text
    x = math.ceil(len(text) / 15)
    y = math.floor(len(text) / x)
    i = y
    j = 0
    while (j < x - 1):
        newtex.insert(i + j, "*")
        j += 1
        i += y
    stringList = ""
    text.pop(0)

    for se in text:
        stringList += se + " "

    return stringList


def split_by_conjuction(text):
    # split by and

    if(len(text)<19):
        return text
    if ("ወይም" in text):
        index = text.index("ወይም")
        text[index] = "ወይም * "
    if ("እና" in text):
        index = text.index("እና")
        text[index] = "እና * "
    if ("ግን" in text):
        index = text.index("ግን")
        text[index] = "ግን * "
    if ("ምክንያቱም" in text):
        index = text.index("ምክንያቱም")
        text[index] = "ምክንያቱም * "
    if ("እንዲሁም" in text):
        index = text.index("እንዲሁም")
        text[index] = "እንዲሁም * "
    if ("ከዚያም" in text):
        index = text.index("ከዚያም")
        text[index] = "ከዚያም * "
    if ("በተጨማሪም" in text):
        index = text.index("በተጨማሪም")
        text[index] = "በተጨማሪም * "

    else:
        return False
    stringList = ""

    for se in text:
        stringList += se + " "



    return stringList


if __name__ == "__main__":
    '''import time
    tic=time.perf_counter()
    fn = "/home/eden/Documents/Articles/Art-1.txt"
    list = generateSegemnts_from_file(fn)

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    count=0
    c1=0
    for l in list:
        count+=len(l.split(" "))
        ov = len(l.split(" "))
        if (ov > 19 or ov < 4):
            c1 += 1
        #print(l)

    validated=validate_generated_segments(list)
    c=0
    o=0
    for v in validated:
        c += len(v.split(" "))
        ov=len(v.split(" "))
        if(ov>19 or ov<4):
            ov+=1
        print(v)
    print("::::::::::::::::::problematic = ::::::::::::::::::::::::::::")
    print(c1)
    print(len(list))

    print("count == "+str(count))
    print("::::::::::::::::::::problematic::::::::::::::::::::::::::")
    print(o)
    toc=time.perf_counter()
    print("time lapsed  = " + str(toc - tic))

    print(len(validated))
    filen = "Articles/Art-"
    i = 1
    from scipy.io import wavfile
    import time
    while (i <= 10):
        fn = filen + str(i) + ".txt"
        print("################################################")
        print("file name = " + fn)
        tic = time.perf_counter()
        se = generateSegemnts_from_file(fn)
        se=validate_generated_segments(se)
        # audio=generate_from_file_w_val(fn)
        toc=time.perf_counter()

        # wavfile.write("Audio_outputs/"+fn+".wav", 21050, np.asarray(audio.data))
        print("COMPLETED in " + str(toc - tic))
        print("################################################")
        i += 1
    

    #print("ALL COMPLETED")
    se = generateSegemnts_from_file(filen+"8.txt")
    se = validate_generated_segments(se)

    o = 0
    for v in se:

        ov = len(v.split(" "))
        if (ov > 19 or ov < 4):
            o += 1
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(v)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        print(v)
    print("################" + str(o) + "################################") '''

    filen = "/home/eden/Desktop/am.txt"

    se = generate_by_psbd(filen)
    print(len(se))
    for m in se:
        print(m)



