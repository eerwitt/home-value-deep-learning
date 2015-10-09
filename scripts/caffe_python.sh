#!/bin/sh

# Helper script to setup a python environment including the caffe libraries.
export PYTHONPATH=/home/ubuntu/caffe/distribute/python
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ubuntu/caffe/distribute/lib:/usr/local/cuda-6.5/lib

exec "/usr/bin/python" "$@"
