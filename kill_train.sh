# helper script to kill train.py

pgrep -f 'python train.py' | xargs kill -9
