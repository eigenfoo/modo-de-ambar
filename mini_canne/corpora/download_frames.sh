# download .npy frames from google cloud storage

if ls lyre_frames.npy > /dev/null 2>&1
then
    echo "lyre_frames.npy found."
else
    echo "lyre_frames.npy not found. Downloading..."
    wget https://storage.googleapis.com/ml_adventure_frames/lyre_frames.npy
fi

if ls cello_frames.npy > /dev/null 2>&1
then
    echo "cello_frames.npy found."
else
    echo "cello_frames.npy not found. Downloading..."
    wget https://storage.googleapis.com/ml_adventure_frames/cello_frames.npy
fi

if ls guitar_frames.npy > /dev/null 2>&1
then
    echo "guitar_frames.npy found."
else
    echo "guitar_frames.npy not found. Downloading..."
    wget https://storage.googleapis.com/ml_adventure_frames/guitar_frames.npy
fi

if ls didgeridoo_frames.npy > /dev/null 2>&1
then
    echo "didgeridoo_frames.npy found."
else
    echo "didgeridoo_frames.npy not found. Downloading..."
    wget https://storage.googleapis.com/ml_adventure_frames/didgeridoo_frames.npy
fi

echo "Success."
