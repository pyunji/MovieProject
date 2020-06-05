from keras.models import Model
from keras.layers import Dense, Embedding, Input, LSTM, TimeDistributed
from keras.models import load_model
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

import data

class Training_seq2seq():
    def __init__(self):
        self.PAD_INDEX = 0
        self.STA_INDEX = 1
        self.END_INDEX = 2
        self.OOV_INDEX = 3

        self.ENCODER_INPUT = 0
        self.DECODER_INPUT = 1
        self.DECODER_TARGET = 2

        self.max_sequences = 60

        self.embedding_dim = 100

        self.lstm_hiddem_dim = 128

        self.chatbot_data = pd.read_csv('./chatbot_data_final.csv'
                                        , encoding='utf-8').dropna()
        self.proc = data.DataProcess()
        self.words = self.proc.vocab
        self.q_train, self.q_test, self.a_train, self.a_test = \
            train_test_split(
                self.chatbot_data['q_morph'].values
                , self.chatbot_data['a_morph'].values
                , train_size=0.8
                , test_size=0.2
                , random_state=0
            )
    def convert_text_to_index(self, sentences, vocabulary, type):
        PAD="<PADDING>"
        STA="<START>"
        END="<END>"
        UNK="<UNK>"
        sentences_index = []
        for sentence in sentences:
            sentence_index = []
            if type == self.DECODER_INPUT:
                sentence_index.extend([vocabulary[STA]])
            for word in sentence.split(' '):
                if vocabulary.get(word) is not None:
                    sentence_index.extend([vocabulary[word]])
                else:
                    sentence_index.extend([vocabulary[UNK]])
            if type == self.DECODER_TARGET:
                if len(sentence_index) >= self.max_sequences:
                    sentence_index = sentence_index[:self.max_sequences-1] + [vocabulary[END]]
                else:
                    sentence_index += [vocabulary[END]]
            else:
                if len(sentence_index) > self.max_sequences:
                    sentence_index = sentence_index[:self.max_sequences]
            sentence_index += (self.max_sequences-len(sentence_index))*[vocabulary[PAD]]
            sentences_index.append(sentence_index)
        return np.asarray(sentences_index, dtype='uint16')

    def train_test_set(self):
        x_encoder_train = self.convert_text_to_index(self.q_train
                                                     , self.proc.word2idx
                                                     , self.ENCODER_INPUT)
        x_encoder_test = self.convert_text_to_index(self.q_test
                                                    , self.proc.word2idx
                                                    , self.ENCODER_INPUT)
        x_decoder_train = self.convert_text_to_index(self.a_train
                                                     , self.proc.word2idx
                                                     , self.DECODER_INPUT)
        x_decoder_test = self.convert_text_to_index(self.a_test
                                                    , self.proc.word2idx
                                                    , self.DECODER_INPUT)
        y_decoder_train = self.convert_text_to_index(self.a_train
                                                     , self.proc.word2idx
                                                     , self.DECODER_TARGET)
        y_decoder_test = self.convert_text_to_index(self.a_test
                                                    , self.proc.word2idx
                                                    , self.DECODER_TARGET)
        y_decoder_train = np.expand_dims(y_decoder_train, 2)
        y_decoder_test = np.expand_dims(y_decoder_test, 2)
        training_set = {'train':{'x_encoder':x_encoder_train
                                , 'x_decoder':x_decoder_train
                                , 'y_decoder':y_decoder_train}
                        , 'test':{'x_encoder':x_encoder_test
                                 , 'x_decoder':x_decoder_test
                                 , 'y_decoder':y_decoder_test}
                         }
        return training_set

    def training_model(self):
        encoder_inputs = Input(shape=(None,), name='encoder_input')
        encoder_embedding = Embedding(self.proc.vocab_len
                                    , self.embedding_dim
                                    , name='encoder_embedding')
        encoder_outputs = encoder_embedding(encoder_inputs)
        encoder_lstm = LSTM(self.lstm_hiddem_dim
                             , dropout=0.1
                             , recurrent_dropout=0.5
                             , return_state=True
                             , name='encoder_LSTM')
        encoder_outputs, hidden_state, cell_state = encoder_lstm(encoder_outputs)
        encoder_states = [hidden_state, cell_state]

        decoder_inputs = Input(shape=(None,), name='decoder_input')
        decoder_embedding = Embedding(self.proc.vocab_len
                                      , self.embedding_dim
                                      , name='decoder_embedding')
        decoder_outputs = decoder_embedding(decoder_inputs)
        decoder_lstm = LSTM(self.lstm_hiddem_dim
                            , dropout=0.1
                            , recurrent_dropout=0.5
                            , return_state=True
                            , return_sequences=True
                            , name='decoder_LSTM')
        decoder_outputs, _, _ = decoder_lstm(decoder_outputs
                                             , initial_state=encoder_states)
        decoder_dense = TimeDistributed(Dense(self.proc.vocab_len
                                              , activation='softmax')
                                        , name='decoder_wrapper')
        decoder_outputs = decoder_dense(decoder_outputs)
        model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
        model.compile(optimizer='adam'
                      , loss='sparse_categorical_crossentropy'
                      , metrics=['sparse_categorical_accuracy'])
        return model

    def run_training(self, load_path=''):
        sets = self.train_test_set()
        x_encoder_train = sets['train']['x_encoder']
        x_encoder_test = sets['test']['x_encoder']
        x_decoder_train = sets['train']['x_decoder']
        x_decoder_test = sets['test']['x_decoder']
        y_decoder_train = sets['train']['y_decoder']
        y_decoder_test = sets['test']['y_decoder']
        if load_path:
            model = load_model(load_path)
        else:
            model = self.training_model()
        early_stopping = EarlyStopping(patience=3)
        history = model.fit([x_encoder_train, x_decoder_train]
                            , y_decoder_train
                            , epochs=10
                            , batch_size=32
                            , callbacks=[early_stopping]
                            , verbose=1
                            , validation_data=([x_encoder_test, x_decoder_test]
                                               , y_decoder_test))
        model.save('./seq2seq_keras.h5')
        print('accuracy :', history.history['sparse_categorical_accuracy'][-1])
        print('loss :', history.history['loss'][-1])




