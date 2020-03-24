#!/usr/bin/python
import tensorflow as tf

from config import Config
from model import CaptionGenerator
from dataset import prepare_train_data, prepare_eval_data, prepare_test_data
from scipy.misc import imread, imresize
from imagenet_classes import class_names
import numpy as np

FLAGS = tf.app.flags.FLAGS

tf.flags.DEFINE_string('phase', 'train',
                       'The phase can be train, eval or test')

tf.flags.DEFINE_boolean('load', False,
                        'Turn on to load a pretrained model from either \
                        the latest checkpoint or a specified file')

tf.flags.DEFINE_string('model_file', None,
                       'If sepcified, load a pretrained model from this file')

tf.flags.DEFINE_boolean('load_cnn', False,
                        'Turn on to load a pretrained CNN model')

tf.flags.DEFINE_string('cnn_model_file', './vgg16_no_fc.npy',
                       'The file containing a pretrained CNN model')

tf.flags.DEFINE_boolean('train_cnn', False,
                        'Turn on to train both CNN and RNN. \
                         Otherwise, only RNN is trained')

tf.flags.DEFINE_integer('beam_size', 3,
                        'The size of beam search for caption generation')

tf.flags.DEFINE_string('image_file','./man.jpg','The file to test the CNN')


## Start token is not required, Stop Tokens are given via "." at the end of each sentence.
## TODO : Early stop functionality by considering validation error. We should first split the validation data.

sess = tf.Session()

def main(argv):
    config = Config()
    config.phase = FLAGS.phase
    config.train_cnn = FLAGS.train_cnn
    config.beam_size = FLAGS.beam_size
    config.trainable_variable = FLAGS.train_cnn

    with tf.Session() as sess:
        data, vocabulary = prepare_test_data(config)
        model = CaptionGenerator(config)
        model.load(sess, FLAGS.model_file)
        tf.get_default_graph().finalize()
        model.test(sess, data, vocabulary)

def start_model():
    import sys
    config = Config()
    config.phase = FLAGS.phase
    config.train_cnn = FLAGS.train_cnn
    config.beam_size = FLAGS.beam_size
    config.trainable_variable = FLAGS.train_cnn
    model = CaptionGenerator(config)
    model.load(sess, "./show_and_tell/models/39999.npy")
    return model

def get_caption(model, image_path):
        data, vocabulary = prepare_test_data(None, [image_path])
        tf.get_default_graph().finalize()
        for caption in model.test(sess, data, vocabulary):
            return caption

if __name__ == '__main__':
    
    tf.app.run()