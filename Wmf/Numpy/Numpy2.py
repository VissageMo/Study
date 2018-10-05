import numpy as np

A = np.arange(2, 14).reshape((3, 4))

# 计算最小元素的索引
print(np.argmin(A))
print(np.argmax(A))

# 计算统计均值

print(np.mean(A))
print(np.average(A))
print(A.mean())

print(np.cumsum(A))  # 第n个数为矩阵前n个元素的和
print(np.nonzero(A))  # 查找非零数，并记录非零元素的索引
print(np.sort(A))  # 逐行排序

print(np.transpose(A))  # 行列转置
print(A.T)  # 同上

print(np.clip(A, 5, 9))  # 将矩阵中小于5的替换成5，大于9的替换为9
