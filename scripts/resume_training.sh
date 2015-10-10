#!/usr/bin/env sh
# Originally found via:
# https://github.com/BVLC/caffe/blob/71e05876f644a08af4cb1c955d01c5a272539e96/examples/imagenet/resume_training.sh

/home/ubuntu/caffe/build/tools/caffe train \
    --solver=/home/ubuntu/prototxt/solver.prototxt \
    --snapshot=/home/ubuntu/snapshots/train_iter_10000.solverstate
