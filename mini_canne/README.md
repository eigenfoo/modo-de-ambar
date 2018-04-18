As it stands: 

- Make a folder named "checkpoints" (no quotes) in whatever directory you drop
  these files into
- train.py trains the neural network (and saves checkpoint files every 3 epochs)
    - --new_init determines whether or not you load previously trained network
      weights The first time you run this, you need to set --new_init=true on
      the cmd line, otherwise the script will not run. After the first run, you
      can decide to load old checkpoint files or start anew
    - --corpus chooses what corpus the network is trained on  as it stands I
      keep all the .npy files as "*_frames.npy", so this argument only needs
      "lyre" or "guitar" or "synth" or (etc)
    - --learning_rate is not yet integrated
    - --optimizer is not yet integrated
    - --loss_function toggles the loss calculation the network uses
        - "sc": spectral convergence, what I have found to work best for the
          network
        - "mse": mean squared error, most common loss function used in deep
          learning
        - "mae": mean absolute error, no one ever uses this and it doesn’t do a
          good job of training the network
- generate.py generates a new soundclip by activating the synthesizer and saves
  it to "loop.wav"
    - can be called even if train.py is running
- play.py will loop the track "loop.wav" for an hour and then close
    - can be called even if generate.py overwrites "loop.wav"
- mini_canne.py is the backbone for all this nonsense
