import torch.nn as nn
import torch
from .Encoder import Conv
from torch.nn import functional as F


class Linear(nn.Module):
    def __init__(self, in_dim, out_dim, bias=True, w_init_gain='linear'):
        super(Linear, self).__init__()
        self.linear_layer = nn.Linear(in_dim, out_dim, bias=bias)

        nn.init.xavier_uniform_(
            self.linear_layer.weight,
            gain=nn.init.calculate_gain(w_init_gain))

    def forward(self, x):
        return self.linear_layer(x)


class Location_layer(nn.Module):
    def __init__(self, n_filters,kernel_size,dim):
        super(Location_layer,self).__init__()
        padding=int((kernel_size-1)/2)
        self.location_conv = Conv(2, n_filters,
                                      kernel_size=kernel_size,
                                      padding=padding, bias=False, stride=1,
                                      dilation=1)
        self.location_dense = Linear(n_filters,dim, bias=False, w_init_gain='tanh')

    def forward(self, attention_weights_cat):
        output = self.location_conv(attention_weights_cat)
        output = output.transpose(1, 2)
        output = self.location_dense(output)
        return output

class Attention(nn.Module):
    def __init__(self, attention_rnn_dim, embedding_dim, attention_dim,
                 attention_location_n_filters, attention_location_kernel_size):
        super(Attention,self).__init__()
        self.query = Linear(attention_rnn_dim, attention_dim,
                                      bias=False, w_init_gain='tanh')
        self.memory = Linear(embedding_dim, attention_dim, bias=False,
                                       w_init_gain='tanh')
        self.v = Linear(attention_dim, 1, bias=False)
        self.location_layer = Location_layer(attention_location_n_filters,
                                            attention_location_kernel_size,
                                            attention_dim)
        self.score_mask_value = -float("inf")

    def get_alignments(self,query,processed_memory, attention_weights_cat):

         processed_query=self.query(query.unsqueeze(1))
         processed_attention=self.location_layer(attention_weights_cat)
         energies=self.v(torch.tanh(processed_attention+processed_memory+processed_query))
         energies = energies.sueeze(-1)
         return energies

    def forward(self, attention_hidden_state, processed_memory,attention_weights_cat, mask,memory):
        alignment = self.get_alignment_energies(
            attention_hidden_state, processed_memory, attention_weights_cat)

        if mask is not None:
            alignment.data.masked_fill_(mask, self.score_mask_value)

        attention_weights = F.softmax(alignment, dim=1)
        attention_context = torch.bmm(attention_weights.unsqueeze(1), memory)
        attention_context = attention_context.squeeze(1)

        return attention_context, attention_weights

