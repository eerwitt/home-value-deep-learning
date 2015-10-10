#!/bin/bash
# Originally found here:
# https://github.com/BVLC/caffe/blob/71e05876f644a08af4cb1c955d01c5a272539e96/examples/imagenet/make_imagenet_mean.sh
/home/ubuntu/caffe/build/tools/compute_image_mean /home/ubuntu/data/train_lmdb \
    /home/ubuntu/data/mean.binaryproto

echo "Done."
