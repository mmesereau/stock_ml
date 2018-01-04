import tensorflow as tf

def simple_network(data_vectors):
    data_placeholder = tf.placeholder(tf.float32, shape=[None, data_vectors[0].length])
    output_placeholder
