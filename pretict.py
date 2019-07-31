from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.layers.core import Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
import numpy as np
from read_data import read_data

data = read_data()

model = Sequential()
model.add(LSTM(5,  activation='relu',  input_shape=(242,3)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
model.fit(data["input"], data["output"], epochs=100, batch_size=10)

model.save('my_model.h5')
