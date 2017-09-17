# -*- coding: utf-8 -*- 
import tensorflow as tf

def sess_12():
    hello = tf.constant('Hello Tensorflow!')
    sess = tf.Session()
    print sess.run(hello)
    a = tf.constant(10)
    b = tf.constant(32)
    print sess.run(a + b)
    print sess.run(a * b)


def main():
    sess_12()

if __name__ == '__main__':
    main()