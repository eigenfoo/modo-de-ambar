# Helper script to call train.py
# python train.py --corpus=lyre --learning_rate=1e-3 --new_init=False --loss_function=sc &

cd mini_canne/
python train.py --corpus=$1 --learning_rate=$2 --new_init=$3 --loss_function=$4 &
