import sys
from mini_canne import *
import os
import argparse

def get_arguments():
  parser = argparse.ArgumentParser(description='SampleRnn example network')
  parser.add_argument('--corpus',  	        type=str,   default='lyre')
  parser.add_argument('--learning_rate',    type=float, default=1e-3)
  parser.add_argument('--optimizer',        type=str,   default='adam', choices=['adam','momentum'])
  parser.add_argument('--new_init', 		type=bool,	default=True)
  parser.add_argument('--loss_function',	type=str,	default='sc',	choices=['sc','mse','mae'])
  return parser.parse_args()

def main():
	args = get_arguments()
	mode = OperationMode(train=True,new_init=args.new_init,control=False)
	synth = ANNeSynth(mode,corpus='corpora/'+args.corpus+'_frames.npy',loss_choice=args.loss_function)
	synth.execute([])
	
	
if __name__ == '__main__':
	main()
