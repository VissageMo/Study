import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:, ['A', 'B']])

# select by position: iloc
print(df.iloc[3])  # 筛选第三行

# mixed selection: ix
print(df.ix[:3, ['A', 'C']])

# 条件筛选
print(df[df.A > 8])  # 筛选 A>8 的行，是完整的行
