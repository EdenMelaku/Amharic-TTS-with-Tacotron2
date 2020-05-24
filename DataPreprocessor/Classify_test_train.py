
import random
import os
class Classifier:
    def __init__(self,hparams, filepath, datasetname):

        with open(filepath, "r") as f:
            data = f.read().split('\n')
        rows = len(data)
        print(rows)
        random.shuffle(data)
        train_num = int(rows * (hparams.train/100))
        test_num = train_num+int(rows * (hparams.test / 100))
        val_num = test_num+int(rows * (hparams.val / 100))
        train_data = data[:train_num]
        test_data = data[train_num:test_num]
        validation_data = data[test_num:val_num]
        '''open("../filelists/"+ datasetname + "/train.txt", "w")
        open("../filelists/"+datasetname + "/test.txt", "w")
        open("../filelists/"+datasetname + "/train.txt", "w")
        '''
        print("######################")
        print("number of train data = " + str(len(train_data)))
        print("number of test data = " + str(len(test_data)))
        print("number of val data = " + str(len(validation_data)))
        print("######################")

        with open("filelists/amharic_audio_text_train_filelist.txt", "w+") as train:
            for i in range(train_num):
                train.write(train_data[i - 1])
                train.write("\n")
        train.close()
        with open("filelists/amharic_audio_text_test_filelist.txt", "w+") as test:
            for i in range(len(test_data)):
                test.write(test_data[i - 1])
                test.write("\n")
        test.close()
        with open("filelists/amharic_audio_text_val_filelist.txt", "w+") as val:
            for i in range(len(validation_data)):
                val.write(validation_data[i - 1])
                val.write("\n")
        val.close()

        print("######################")
