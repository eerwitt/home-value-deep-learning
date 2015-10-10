#!/bin/bash
# Run the full process to go from a bunch of images and their test, train, cross validation and their friendly words (SOFTMAX loss layer) to a trained caffe model.
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ubuntu/caffe/distribute/lib:/home/ubuntu/torch-distro/install/lib:/home/ubuntu/torch-distro/install/lib:/usr/local/cuda/lib64:
echo "Warning, removing generated data directory before running Caffe."

rm -Rf /home/ubuntu/data/mean.binaryproto /home/ubuntu/data/mean.npy /home/ubuntu/data/train_lmdb /home/ubuntu/data/val_lmdb

(sudo ln /dev/null /dev/raw1394) || echo "raw1394 can't be linked, OK to ignore."

./create_lmbd.sh
./make_mean.sh
./convert_protomean.py /home/ubuntu/data/mean.binaryproto /home/ubuntu/data/mean.npy
./train.sh
