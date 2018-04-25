# Helper script to call generate.py
# python generate.py --LFO_Rate=40 --n_frames=2500

cd mini_canne/
python generate.py --LFO_Rate=$1 --n_frames=$2 &
