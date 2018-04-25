import numpy as np
import matplotlib.pyplot as plt
import librosa
import os


bass_boost = (np.exp(np.linspace(1, -20, 2049)))
bass_boost = np.ones(2049)
bass_boost[100:] *= np.cos(np.linspace(0, np.pi / 2, len(bass_boost[100:])))
x_axis = np.arange(2049)
plt.figure()
plt.plot(x_axis, bass_boost)
plt.show()
