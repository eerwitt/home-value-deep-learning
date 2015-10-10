#!/usr/bin/env sh
# Start training and log to a file in the home directory.
# Originally found via:
# https://github.com/BVLC/caffe/blob/71e05876f644a08af4cb1c955d01c5a272539e96/examples/imagenet/train_caffenet.sh
nohup /home/ubuntu/caffe/build/tools/caffe train \
    --solver=/home/ubuntu/prototxt/solver.prototxt > /home/ubuntu/logs/training.log &
disown
