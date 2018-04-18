import sys
from mini_canne import *
import os

mode = OperationMode(train=True,new_init=False,control=False)
synth = ANNeSynth(mode,corpus='corpora/lyre_frames.npy')

def main():
	synth.load_weights_into_memory()
	vals = np.random.uniform(low=0.45, high=0.55, size=(1,17))
	vals[:,16] = 0
	synth.play_synth(vals,n_frames=1500,LFO=True)
	
	
if __name__ == '__main__':
	main()
