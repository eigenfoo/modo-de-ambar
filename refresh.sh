# helper script to call train.py
# python train.py --corpus=lyre --learning_rate=1e-3 --new_init=False --loss_function=sc &

cd mini_canne/
rm checkpoints/*
python train.py --corpus=lyre --learning_rate=1e-3 --new_init=True --loss_function=sc &
sleep 20
pkill python
python generate.py
