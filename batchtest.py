
import numpy as np
import torch

from Tacotron_hparams import Create

from train import load_model
from text import text_to_sequence
from process_text import generateSegemnts_from_file,validate_generated_segments, generate_by_psbd
import time
tic = time.perf_counter()

hparams = Create()
waveglow = "waveglow_256channels_universal_v5.pt"
tacotron = "tacotron2_statedict.pt"
hparams.sampling_rate = 22050
print("loading tacotron model")
model = load_model(hparams)
model.load_state_dict(torch.load(tacotron)['state_dict'])
_ = model.cuda().eval().half()
from waveglow_NVIDIA.denoiser import Denoiser
print("loading waveglow model")
waveglow = torch.load(waveglow)['model']
waveglow.cuda().eval().half()
for k in waveglow.convinv:
    k.float()
denoiser = Denoiser(waveglow)
toc = time.perf_counter()
print("time lapsed for model initiation = "+str(toc-tic))

def generate_W_seg(filename):
    sentences=generate_by_psbd(filename)
    audio=batch_inference(sentences)
    return audio


def generate_from_file(file_name):
        sentences=generateSegemnts_from_file(file_name)
        audio=batch_inference(sentences)
        return audio

def generate_from_file_w_val(file_name):
        tic1=time.perf_counter()
        sentences=generateSegemnts_from_file(file_name)
        sentences=validate_generated_segments(sentences)
        toc1=time.perf_counter()
        tic2=time.perf_counter()
        audio=batch_inference(sentences)
        toc2=time.perf_counter()
        print("number of sentences = "+str(len(sentences)))
        c=0
        for l in sentences:
            c+=len(l.split(" "))
        print("number of characters = "+str(c))
        print("time to generate sentence segments = " + str(toc1 - tic1))
        print("time to process Audio segments = " + str(toc2 - tic2))
        return audio


def batch_inference(sentences):


     import time
     print("processing text")
     import wave
     i=0
     au = np.array([])
     leng=len(sentences)
     warning = 0
     while i<leng:

             sequence = np.array(text_to_sequence(sentences[i], ['english_cleaners']))[None, :]
             sequence = torch.autograd.Variable(
                 torch.from_numpy(sequence)).cuda().long()

             mel_outputs, mel_outputs_postnet, _, alignments,is_max = model.inference(sequence)
             if(len(mel_outputs) == hparams.max_decoder_steps):
                 warning+=1
             if(warning==3):
                 print("the system have encountered processing this sentence ")
                 print("#####################################################")
                 print(sentences[i])
                 print("#####################################################")
                 print("Aborting....")
                 break

             else:
               warning=0
               i+=1
               with torch.no_grad():
                  audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
                  audio_denoised = denoiser(audio, strength=0.01)[:, 0]
                  au = np.concatenate((au, audio_denoised.cpu().numpy()), axis=None)

     return au








if __name__ == '__main__':
    filen="Articles/Art-"
    i=1
    from scipy.io import wavfile
    while (i<=10):
       fn=filen+str(i)+".txt"
       print("################################################")
       print("file name = "+fn)
       tic=time.perf_counter()
       se=generate_from_file_w_val(fn)
       #audio=generate_from_file_w_val(fn)
       #toc=time.perf_counter()
       #wavfile.write("Audio_outputs/"+fn+".wav", 21050, np.asarray(audio.data))
       print("COMPLETED in "+str(toc-tic))
       print("################################################")
       i+=1

    print("ALL COMPLETED")
