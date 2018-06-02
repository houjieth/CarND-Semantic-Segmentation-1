import tensorflow as tf

with tf.Session() as sess:
    tf.saved_model.loader.load(sess, ['vgg16'], 'data/vgg')
    writer = tf.summary.FileWriter('.', sess.graph)
    writer.close()

print('done')
