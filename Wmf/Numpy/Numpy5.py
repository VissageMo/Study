import numpy as np

A = np.arange(12).reshape((3, 4))

B = np.split(A, 2, axis=1)  # 纵向分割为2块
C = np.split(A, 3, axis=0)  # 横向分割为3块

D = np.array_split(A, 3, axis=1)  # 不等项分割

E = np.vsplit(A, 3)
F = np.hsplit(A, 2)

