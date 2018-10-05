import numpy as np

A = np.arange(3, 15).reshape((3, 4))
print(A)
print('\n', A[2])
print('\n', A[2][1])
print('\n', A[2, 1])
print('\n', A[:, 2])
print('\n', A[1, 1:3])

for column in A.T:  # 用 for 函数按行或按列切片
    print('\n', column)

for pigu in A:
    print('\n', pigu)

print('\n', A.flatten())  # flatten, 迭代器， 将矩阵变为一行元素
for item in A.flat:
    print(item)

