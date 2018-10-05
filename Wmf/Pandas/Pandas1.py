import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
dates = pd.date_range('20180723', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20180623'),
                    'C': pd.Series(1,index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "hello", "test"]),
                    'F': 'Foo'})

# print(df2.dtypes)  # 数据类型
# print(df2.index)  # 列序号
# print(df2.columns)  # 数据名称
# print(df2.values)  # 只查看所有的值
# print(df2.describe())  # 数据总结
# print(df2.T)  # 翻转
print(df2.sort_index(axis=1, ascending=False))  # ascending(True/False),正倒排序；axis（0/1），行列排序
print(df2.sort_values(by='E'))  # 针对某行的值进行排序

