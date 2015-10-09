#!/usr/bin/env sh
# Originally found via:
# https://github.com/BVLC/caffe/blob/71e05876f644a08af4cb1c955d01c5a272539e96/examples/imagenet/resume_training.sh

../caffe/build/tools/caffe train \
    --solver=../prototxt/solver.prototxt \
    --snapshot=../snapshots/train_iter_10000.solverstate
