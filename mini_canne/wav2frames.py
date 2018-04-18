import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import pickle
import os
import librosa
import librosa.display
import scipy as sci

len_window = 4098 #Specified length of analysis window
hop_length_ = 1024 #Specified percentage hop length between windows

filename_in = 'all_solos_44k.wav'
filename_out = 'guitar_frames'
data_path = os.path.join(os.getcwd(),filename_in)
y, sr = librosa.load(data_path, sr=44100)

D = librosa.stft(y,n_fft=len_window, window='hann')
print(D.shape)
temp = D[:,:]
temp = np.abs(temp)
temp = temp / (temp.max(axis=0)+0.000000001)
print(temp.max(axis=0))
temp = np.transpose(temp)
print(np.shape(temp))
output = temp[~np.all(temp == 0, axis=1)]
print(np.shape(output))
np.save(filename_out+'.npy',output)

