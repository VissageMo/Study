import tensorflow as tf
import numpy as np
import struct

train_image_path = '/home/mo/Documents/PcProject/py3.6/Dataset/MNIST-data/train-images-idx3-ubyte.gz'
train_label_path = '/home/mo/Documents/PcProject/py3.6/Dataset/MNIST-data/train-labels-idx1-ubyte.gz'


def decode_idx3_ubyte(idx3_ubyte_file, status, saveflag=False):

    train_image = open(train_image_path, 'rb')
    buf = train_image.read()

    index = 0
    magic, imageNum, rows, cols = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')
    image = np.empty((imageNum, rows, cols))
    image_size = rows * cols

    # define how many numbers(size of photo) to get for one time
    fmt = '>' + str(image_size) + 'B'

    for i in range(imageNum):
        im = struct.unpack_from(fmt, buf, index)
        im = np.reshape(im, [rows, cols])
        image[i] = np.array(im)

        if saveflag:
            im = image.from_array(np.unit8(image[i]))
            im.save(status + str(i) + '.png')

        index += struct.calcsize(fmt)

    return image




