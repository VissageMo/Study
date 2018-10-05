import numpy as np

a = np.arange(4)
b = a.copy()  # deep copy, 赋值但并不关联
c = a
d = b

a[0] = 11  # 赋值为同一个变量，改变 a 会全部改变 b c d
d[1:3] = [22, 33]  # 赋值为同一个变量，改变 d 会全部改变 b c a




