# Selling a Home with Deep Learning

Work flow used to build a model which can estimate a home's value based on an image of the home.

This can be used as a base project to launch off custom projects which use deep learning to build complex models used in estimating.

The work flow is designed with the following goals in mind.

* Keep it affordable.
* Quickly iterate (__not hack!__).
* Provable assertions.

The general process which is used in building these models follows a general pattern of:

* Download a bunch of images.
* Get or create meta-data about the images.
* Train a Convolutional Neural Network using these images.
* Visualize the results.
* Tweak parameters.
* Do it all again.

## Setup Requirements

This is a Python project which works best on Python 2.7 but *should* work on Python 3.0 as well.

Mostly you'll need requirements in the main project but sub-projects will have separate requirements.

`pip install -r requirements.txt`

Now startup the notebooks and look around.

`ipython notebook`

## Process

![General Architecture](./docs/images/general-layout.png?raw=true "General Architecture")

### General Operations

Manage the system or systems which are doing the model training.

* Check list of prices for EC2 Spot instances g2.2xlarge.
* Start a spot instance in a certain region for _x_ hours or days.
* Use Ansible to connect to system and be able to transfer files.
  * Get logs from system.
  * Run python script to get filters for a snapshot.
* Get filter and logs from system.
* Visualize results in iPython notebook.
* Shutdown instance.


### Training Data Setup

Create data which will be used to create a model.

* Generate test, train and cross validation data.
  * Connect to Zillow and download pictures.
  * Categorize images using `categorization` Django application.
  * Output in a format for Caffe to use.


## References

* [Excellent Introduction to CNN](https://www.youtube.com/watch?v=bEUX_56Lojc)
* [Deeper Tutorial on CNN](http://cs231n.github.io/convolutional-networks/)
* [Caffe Layers](http://caffe.berkeleyvision.org/tutorial/layers.html)
* [Caffe MNIST Tutorial](http://caffe.berkeleyvision.org/gathered/examples/mnist.html)
* [Applications of Convolutions](https://en.wikipedia.org/wiki/Convolution#Applications)
* [Complexities of Convolutions](https://github.com/Yangqing/caffe/wiki/Convolution-in-Caffe:-a-memo)
* [MXNet Distributed Deep Learning](https://github.com/dmlc/mxnet)
* [RNN Introduction](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
* [Chainer Deep Learning Framework](http://chainer.org/)
