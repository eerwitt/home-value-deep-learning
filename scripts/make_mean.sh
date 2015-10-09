#!/usr/bin/env sh
# Originally found here:
# https://github.com/BVLC/caffe/blob/71e05876f644a08af4cb1c955d01c5a272539e96/examples/imagenet/make_imagenet_mean.sh
../caffe/build/tools/compute_image_mean ../data/train_lmdb \
    ../data/mean.binaryproto

echo "Done."
