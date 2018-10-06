import tensorflow as tf

with tf.name_scope('a_name_scope') as scope:
    initializer = tf.constant_initializer(value=1)
    var1 = tf.get_variable(name='var1', shape=[1], dtype=tf.float32, initializer=initializer)
    var2 = tf.Variable(name='var2', initial_value=[2], dtype=tf.float32)
    var2 = tf.Variable(name='var2', initial_value=[4], dtype=tf.float32)

with tf.variable_scope('b_name_scope') as scope:
    initializer = tf.constant_initializer(value=3)
    var3 = tf.get_variable(name='var3', initial_value=[4], dtype=tf.float32, initializer=initializer)
    scope.reuse_variables()
    vars_reuse = tf.get_variable(name='var3')
    var4 = tf.Variable(name='var4', initial_value=[4], dtype=tf.float32)
    var4 = tf.Variable(name='var4', initial_value=[4], dtype=tf.float32)