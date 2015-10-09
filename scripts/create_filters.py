#!/home/ubuntu/scripts/caffe_python.sh
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

caffe.set_mode_cpu()

net = caffe.Net(
    "../prototxt/deploy.prototxt",
    "../snapshots/train_iter_20000.caffemodel",
    caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))

transformer.set_mean('data', np.load('../data/mean.npy').mean(1).mean(1))

transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))

net.blobs['data'].reshape(1, 3, 227, 227)
net.blobs['data'].data[...] = transformer.preprocess(
    'data',
    caffe.io.load_image("../images/IS1jvzv15ey9fr0000000000.jpg"))

out = net.forward()
print("Predicted class is #{}.".format(out['prob'].argmax()))


def vis_square(data, padsize=1, padval=0):
    data -= data.min()
    data /= data.max()

    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (
        (0, n ** 2 - data.shape[0]),
        (0, padsize),
        (0, padsize)) + ((0, 0),) * (data.ndim - 3)

    data = np.pad(
        data,
        padding,
        mode='constant',
        constant_values=(padval, padval))

    data = data.reshape((n, n) + data.shape[1:]).transpose(
        (0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])

    plt.imshow(data)

filters = net.params['conv1'][0].data
vis_square(filters.transpose(0, 2, 3, 1))

plt.savefig("../data/filter-1.png", bbox_inches='tight')
