# coding: utf-8
# by alex
import numpy as np
import matplotlib.pylab as plt


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)  #-c是为了解决溢出问题
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

x = np.arange(-5.0, 5.0, 0.1)
y = softmax(x)
plt.plot(x, y,label="softmax")
plt.xlabel("input") # x轴的标签
plt.ylabel("output") # y轴的标签
plt.title('softmax demo')
plt.show()
