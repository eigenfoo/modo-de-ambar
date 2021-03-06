# modo de ámbar

A text-based adventure game that uses a neural network to generate audio.

Also be sure to check out the [manual for the
game](https://github.com/eigenfoo/modo-de-ambar/blob/master/doc/manual.pdf)!

## Requirements

- Python 3
- Tensorflow (included in `requirements.txt`)
- `pgrep` UNIX utility

## Setup

```
git clone https://github.com/eigenfoo/ml-adventure.git
cd ml-adventure/
pip install -r requirements.txt
cd mini_canne/corpora/
./download_frames.sh
cd ../../
```

## Usage

```
python game.py
```

## License

`adventurelib` is made available by Daniel Pope through the MIT License
[here](https://github.com/lordmauve/adventurelib).

The remainder of this software is released under the Apache License 2.0.
