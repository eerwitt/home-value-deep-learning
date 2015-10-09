# Scripts!

The scripts in this directory are used by Caffe on the instance. These are synced in the `../Request Caffe Spot Instance.ipynb` file to the instance which is hosting Caffe.

## run_all.sh

Run all the steps required to start training based on a few pieces of information existing first. This requires:

  Image files located under ../images
  Computed files located under ../computed
  Output located under ../data

This will resize images and add them to Lightening Memory Mapped DB files which are used by Caffe in the "data" layer.
