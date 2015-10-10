#!/bin/bash

# Helper script to setup a python environment including the caffe libraries.
export PYTHONPATH=/home/ubuntu/caffe/distribute/python
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ubuntu/caffe/distribute/lib:/home/ubuntu/torch-distro/install/lib:/home/ubuntu/torch-distro/install/lib:/usr/local/cuda/lib64:

exec "/usr/bin/python" "$@"
