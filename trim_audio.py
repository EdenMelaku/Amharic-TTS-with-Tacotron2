# FROM https://stackoverflow.com/questions/29547218/remove-silence-at-the-beginning-and-at-the-end-of-wave-files-with-pydub
# https://github.com/Yeongtae/tacotron2/blob/master/preprocess_audio.py
import glob
from pydub import AudioSegment
"""
This code was developed with reference to https://github.com/Rayhane-mamah/Tacotron-2.
"""
from scipy.io.wavfile import write
import librosa
import numpy as np
import argparse

sr = 22050
max_wav_value=32768.0
trim_fft_size = 1024
trim_hop_size = 256

# These are control parameters for trimming and skipping
trim_top_db = 23
skip_len = 14848

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def preprocess_audio(file_list, silence_audio_size, pre_emphasis=False, newlocation="new/"):
    for file in file_list:
        data, sampling_rate = librosa.core.load(file, sr)
        data = data / np.abs(data).max() *0.999
        data_= librosa.effects.trim(data, top_db= trim_top_db, frame_length=trim_fft_size, hop_length=trim_hop_size)[0]
        if (pre_emphasis):
            data_ = np.append(data_[0], data_[1:] - 0.97 * data_[:-1])
            data_ = data_ / np.abs(data_).max() * 0.999
        data_ = data_ * max_wav_value
        data_ = np.append(data_, [0.]*silence_audio_size)
        data_ = data_.astype(dtype=np.int16)
        # print(i.split('/')[-1])
        write(newlocation + file.split('/')[-1], sr, data_)
        #print(len(data),len(data_))
        if(i%100 == 0):
            print (i)

def remove_short_audios(file_name):
    f = open(file_name,'r',encoding='utf-8')
    R = f.readlines()
    f.close()

    L = []
    for i, r in enumerate(R):
        wav_file = r.split('|')[0]
        data, sampling_rate = librosa.core.load(wav_file, sr)
        if(len(data) >= skip_len):
            L.append(r)
        if (i % 100 == 0):
            print(i)
    tmp = file_name.split('.')
    tmp.insert(1,'_skipped.')
    skipped_file_name = "".join(tmp)
    f = open(skipped_file_name,'w',encoding='utf-8')
    f.writelines(L)
    f.close()

if __name__ == "__main__":
    """
    usage
    python preprocess_dataset.py -f=metadata.csv -s=5 -t -p -r
    python preprocess_dataset.py -f=metadata.csv
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filelist', type=str,
                        help='Metadata file list to preprocess')
    parser.add_argument('-s', '--silence_padding', type=int, default=0,
                        help='Adding silence padding at the end of each audio, silence audio size is hop_length * silence padding')
    parser.add_argument('-p', '--pre_emphasis', action='store_true',
                        help="Doing pre_emphasis")
    parser.add_argument('-t', '--trimming', action='store_true',
                        help="Doing trimming audios")
    parser.add_argument('-r', '--remove_short_audios',action='store_true',
                        help="Removing short audios in metadata file")
    parser.add_argument('-x', '--remove_start_end',action='store_true',
                        help="Removing silence from start and end")
    args = parser.parse_args()
    filelist = glob.glob(args.filelist +'/*.wav')
    silence_audio_size = trim_hop_size * args.silence_padding

    preprocess_audio(filelist, silence_audio_size, args.pre_emphasis)

    if(args.remove_short_audios):
        for f in filelist:
            remove_short_audios(f)

    if(args.remove_start_end):
        for i in filelist:
            sound = AudioSegment.from_file(i, format="wav")

            start_trim = detect_leading_silence(sound)
            end_trim = detect_leading_silence(sound.reverse())

            print("Remove this much from start from file {} : {} and {} from the end".format(i, start_trim, end_trim))
            duration = len(sound)
            trimmed_sound = sound[start_trim:duration-end_trim]
        # print(i.split('/')[-1])
        # trimmed_sound.export("test_split/"+i.split('/')[-1], format="wav")
