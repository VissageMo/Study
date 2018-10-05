import numpy as np

array = np.array([[1, 2, 3], [2, 3, 4]])

print(array)
print('number of dim:', array.ndim)  # ndim：维度
print('shape:', array.shape)  # shape：行列
print('size:', array.size)  # size：元素个数

a = np.array([[2, 23, 4], [2, 32, 4]], dtype=np.int)    # np.int64, np.int32, np.float32, np.float64

b = np.zeros((3, 4))
c = np.ones((3, 4))
d = np.empty((3, 4))

e = np.arange(10, 20, 2)
f = np.arange(12).reshape((3, 4))
g = np.linspace(1, 10, 20)

h = np.array([10, 20, 30, 40])
i = np.arange(4)
j = h-i

k = 10 * np.sin(a)

print(i < 3)  # i > 3, i == 3

l = np.array([[1, 1], [0, 1]])
m = np.arange(4).reshape((2, 2))
n = l * m  # 矩阵对应元素相乘
n_dot = np.dot(l, m)  # 矩阵乘积
n_dot_2 = l.dot(m)  # 和上一行一样

o = np.random.random((2, 4))
print(o)
print(np.sum(o, axis=1))   # axis=0,在行中运算； axis=1，在列中运算; 不设就是全局运算
print(np.min(o, axis=0))
print(np.max(o))



