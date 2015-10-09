#!/bin/sh
# Run the full process to go from a bunch of images and their test, train, cross validation and their friendly words (SOFTMAX loss layer) to a trained caffe model.
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ubuntu/caffe/distribute/lib:/usr/local/cuda-6.5/lib
sudo ln /dev/null /dev/raw1394
./create_lmbd.sh
./make_mean.sh
./convert_protomean.py ../data/mean.binaryproto ../data/mean.npy
./train.sh
