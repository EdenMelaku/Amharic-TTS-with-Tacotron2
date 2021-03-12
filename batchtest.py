import numpy as np
import torch

from Tacotron_hparams import Create

from train import load_model
from text import text_to_sequence
from process_text import generateSegemnts_from_file, validate_generated_segments, generate_by_psbd
import time
from DataPreprocessor import TacotronSTFT as STFT


class Denoiser(torch.nn.Module):
    """ Removes model bias from audio produced with waveglow """
    def __init__(self, waveglow, filter_length=1024, n_overlap=4,
                 win_length=1024, mode='zeros'):
        super(Denoiser, self).__init__()
        self.stft = STFT.STFT(filter_length=filter_length,
                              hop_length=int(filter_length / n_overlap),
                              win_length=win_length).cuda()
        if mode == 'zeros':
            mel_input = torch.zeros(
                (1, 80, 88),
                dtype=waveglow.upsample.weight.dtype,
                device=waveglow.upsample.weight.device)
        elif mode == 'normal':
            mel_input = torch.randn(
                (1, 80, 88),
                dtype=waveglow.upsample.weight.dtype,
                device=waveglow.upsample.weight.device)
        else:
            raise Exception("Mode {} if not supported".format(mode))

        with torch.no_grad():
            bias_audio = waveglow.infer(mel_input, sigma=0.0).float()
            bias_spec, _ = self.stft.transform(bias_audio)

        self.register_buffer('bias_spec', bias_spec[:, :, 0][:, :, None])

    def forward(self, audio, strength=0.1):
        audio_spec, audio_angles = self.stft.transform(audio.cuda().float())
        audio_spec_denoised = audio_spec - self.bias_spec * strength
        audio_spec_denoised = torch.clamp(audio_spec_denoised, 0.0)
        audio_denoised = self.stft.inverse(audio_spec_denoised, audio_angles)
        return audio_denoised


tic = time.perf_counter()

hparams = Create()
waveglow = "/content/drive/MyDrive/AmhTTS with new checkpoint/waveglow_268000"
tacotron = "/content/drive/MyDrive/AmhTTS with new checkpoint/checkpoint_147000"
hparams.sampling_rate = 22050
print("loading tacotron model")
model = load_model(hparams)
model.load_state_dict(torch.load(tacotron)['state_dict'])
_ = model.cuda().eval().half()
# from waveglow_NVIDIA.denoiser import Denoiser
print("loading waveglow model")
waveglow = torch.load(waveglow)['model']
waveglow.cuda().eval().half()
for k in waveglow.convinv:
    k.float()
denoiser = Denoiser(waveglow)
toc = time.perf_counter()
print("time lapsed for model initiation = " + str(toc - tic))


def generate_W_seg(filename):
    sentences = generate_by_psbd(filename)
    audio = batch_inference(sentences)
    return audio


def generate_from_file(file_name):
    sentences = generateSegemnts_from_file(file_name)
    audio = batch_inference(sentences)
    return audio


def generate_from_file_w_val(file_name):
    tic1 = time.perf_counter()
    sentences = generateSegemnts_from_file(file_name)
    sentences = validate_generated_segments(sentences)
    toc1 = time.perf_counter()
    tic2 = time.perf_counter()
    audio = batch_inference(sentences)
    toc2 = time.perf_counter()
    print("number of sentences = " + str(len(sentences)))
    c = 0
    for l in sentences:
        c += len(l.split(" "))
    print("number of characters = " + str(c))
    print("time to generate sentence segments = " + str(toc1 - tic1))
    print("time to process Audio segments = " + str(toc2 - tic2))
    return audio


def batch_inference(sentences):
    import time
    print("processing text")
    import wave
    i = 0
    au = np.array([])
    leng = len(sentences)
    warning = 0
    while i < leng:

        sequence = np.array(text_to_sequence(sentences[i], ['english_cleaners']))[None, :]
        sequence = torch.autograd.Variable(
            torch.from_numpy(sequence)).cuda().long()

        mel_outputs, mel_outputs_postnet, _, alignments, is_max = model.inference(sequence)
        if (len(mel_outputs) == hparams.max_decoder_steps):
            warning += 1
        if (warning == 3):
            print("the system have encountered processing this sentence ")
            print("#####################################################")
            print(sentences[i])
            print("#####################################################")
            print("Aborting....")
            break

        else:
            warning = 0
            i += 1
            with torch.no_grad():
                audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
                audio_denoised = denoiser(audio, strength=0.01)[:, 0]
                au = np.concatenate((au, audio_denoised.cpu().numpy()), axis=None)

    return au


if __name__ == '__main__':
    filen = "Articles/Art-"
    i = 1
    from scipy.io import wavfile

    while (i <= 10):
        fn = filen + str(i) + ".txt"
        print("################################################")
        print("file name = " + fn)
        tic = time.perf_counter()
        se = generate_from_file_w_val(fn)
        # audio=generate_from_file_w_val(fn)
        # toc=time.perf_counter()
        # wavfile.write("Audio_outputs/"+fn+".wav", 21050, np.asarray(audio.data))
        print("COMPLETED in " + str(toc - tic))
        print("################################################")
        i += 1

    print("ALL COMPLETED")
