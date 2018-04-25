import sys
from mini_canne import *
import os
import argparse

mode = OperationMode(train=True, new_init=False, control=False)
synth = ANNeSynth(mode, corpus='corpora/lyre_frames.npy')


def get_arguments():
    parser = argparse.ArgumentParser(description='SampleRnn example network')
    parser.add_argument('--LFO_Rate', type=float, default='50')
    parser.add_argument('--n_frames', type=int, default='1000')
    return parser.parse_args()


def main():
    args = get_arguments()
    synth.load_weights_into_memory()
    vals = np.random.uniform(low=0.35, high=0.45, size=(1, 17))
    vals[:, 16] = 0
    synth.play_synth(vals, n_frames=args.n_frames, LFO=args.LFO_Rate)


if __name__ == '__main__':
    main()
