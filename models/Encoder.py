from torch import nn
from torch.nn import functional as F

class Conv(nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size=1, stride=1,
                 padding=None, dilation=1, bias=True, w_init_gain='linear'):
        super(Conv, self).__init__()
        if padding is None:
            assert (kernel_size%2 == 1)
            padding=int(dilation * (kernel_size - 1)/2)
            self.con=nn.Conv1d(in_channels,out_channels,kernel_size=kernel_size,stride=stride,padding=padding,dilation=dilation,bias=bias)
            nn.init.xavier_uniform(self.con.weight, gain=nn.init.calculate_gain(w_init_gain))

    def forward(self,signal):
        conv_signal=self.con(signal)
        return conv_signal


class Encoder(nn.Module):

    def __init__ (self,hparams):
        super(Encoder,self).__init__()
        convolutions=[]
        for i in range(hparams.encoder_n_convolutions):
            conv_layer=nn.Sequential(
                 Conv(hparams.encoder_embedding_dim,
                            hparams.encoder_embedding_dim,
                            kernel_size = hparams.encoder_kernel_size, stride=1,
                            padding = int((hparams.encoder_kernel_size - 1)/2),
                            dilation = 1, w_init_gain='relu'),
                 nn.BatchNorm1d(hparams.encoder_embedding_dim))
            convolutions.append(conv_layer)

        self.convolutions = nn.ModuleList(convolutions)

        self.lstm=nn.LSTM(hparams.encoder_embedding_dim, int(hparams.encoder_embedding_dim/2), 1, batch_first=True, bidirectional = True)


    def forward(self,x, input_len):

        for convl in self.convolutions:
            x=F.dropout(F.relu(convl(x)), 0.5,  self.traning)

        x = x.transpose(1, 2)

        # pytorch tensor are not reversible, hence the conversion
        input_lengths = input_len.cpu().numpy()
        x = nn.utils.rnn.pack_padded_sequence(
            x, input_lengths, batch_first=True)

        self.lstm.flatten_parameters()
        outputs, _ = self.lstm(x)

        outputs, _ = nn.utils.rnn.pad_packed_sequence(
            outputs, batch_first=True)

        return outputs

    def inference(self, x):

        for conv in self.convolutions:
            x = F.dropout(F.relu(conv(x)), 0.5, self.training)

        x = x.transpose(1, 2)

        self.lstm.flatten_parameters()
        outputs, _ = self.lstm(x)

        return outputs




