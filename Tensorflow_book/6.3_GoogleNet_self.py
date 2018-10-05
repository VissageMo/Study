import tensorflow as tf


# save the kernel and biases in p
def conv2_op(input_op, name, n_out, kh, kw, dh, dw, p=p, padding='SAME'):
    n_in = input_op.get_shape()[-1].value

    with tf.name_scope(name) as scope:
        kernel = tf.get_variable(scope+"w", shape=[kh, kw, n_in, n_out], dtype=tf.float32,
                                 initializer=tf.contrib.layers.xavier_initializer_conv2d())

        conv = tf.nn.conv2d(input_op, kernel, (1, dh, dw, 1), padding=padding)
        bias_init_val = tf.constant(0.0, shape=[n_out], dtype=tf.float32)
        biases = tf.Variable(bias_init_val, trainable=True, name='b')
        z = tf.nn.bias_add(conv, biases)
        activation = tf.nn.relu(z, name=scope)
        p += [kernel, biases]
        return activation


def fc_op(input_op, name, n_out, p):
    n_in = input_op.get_shape()[-1].value
    with tf.name_scope(name) as scope:
        kernel = tf.get_variable(scope+"w", shape=[n_in, n_out], dtype=tf.float32,
                                 initializer=tf.contrib.layers.xavier_initializer())
        biases = tf.Variable(tf.constant(0.1, shape=[n_out], dtype=tf.float32), name='b')
        activation = tf.nn.relu_layer(input_op, kernel, biases, name=scope)
        p += [kernel, biases]
        return activation


def mpool_op(input_op, name, kh, kw, dh, dw, padding='SAME'):
    return tf.nn.max_pool(input_op, ksize=[1, kh, kw, 1], strides=[1, dh, dw, 1],
                          padding=padding, name=name)


def apool_op(input_op, name, kh, kw, dh, dw, padding='SAME'):
    return tf.nn.avg_pool(input_op, ksize=[1, kh, kw, 1], strides=[1, dh, dw, 1],
                          padding=padding, name=name)


def googlenet_op(input_op):
    p1 = []
    net = conv2_op(input_op, 'conv_1a_7x7', 64, 7, 7, 2, 2, p1, padding='VALID')
    net = conv2_op(net, 'conv_1b_3x3', 32, 3, 3, 1, 1, p1, padding='VALID')
    net = conv2_op(net, 'conv1_1c_3x3', 32, 3, 3, 1, 1, p1)
    net = mpool_op(net, 'mpool_1d_3x3', 3, 3, 2, 2)






