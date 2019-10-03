# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-10-02 21:52:43
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-10-02 21:52:43
import tensorflow as tf
hello = tf.constant('hello,tensorf')
sess = tf.Session()
print(sess.run(hello))
