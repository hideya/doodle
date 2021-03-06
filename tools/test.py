import sys

import six
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity('DEBUG')

def train(src_dir, config):
    sys.path.append(src_dir)
    import doodle as dd

    params = {
        'train_tfrecord_file' : 'train.tfr',
        'test_tfrecord_file'  : 'test.tfr',
    }

    model_fn = dd.model_fn
    train_input_fn = lambda: dd.train_input_fn('./data', params)
    eval_input_fn  = lambda: dd.eval_input_fn('./data', params)

    e = tf.estimator.Estimator(
        model_fn=model_fn,
        model_dir=config.get('model_dir', None),
        params=params)
    e.train(train_input_fn, max_steps=config.get('max_steps', 10))

    metrics = e.evaluate(eval_input_fn, steps=1)
    print('###### metrics ' + '#' * 65)
    for name, value in six.iteritems(metrics):
        print('{:<30}: {}'.format(name, value))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-dir')
    parser.add_argument('-m', '--model-dir')
    parser.add_argument('--max-steps', type=int, default=10)
    args = parser.parse_args()
    config = dict(
        model_dir=args.model_dir,
        max_steps=args.max_steps,
    )
    train(args.source_dir, config)
