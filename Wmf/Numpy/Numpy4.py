import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B))  # 上下合并矩阵 vertical stack
D = np.hstack((A, B))  # 左右合并矩阵 horizontal stack

E = (A[:, np.newaxis])  # 横向转纵向，注意不能使用 A.T
F = np.concatenate((A, B, B, A), axis=0)


