shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])  # -1指该序列的最后一项
print('Item -2 is',shoplist[-2])
print('Character 0 is', name[0])

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 设定起止点的切片
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 设定步长的切片
print(shoplist[::1])
print(shoplist[::2])  # 0 2 4....
print(shoplist[::3])  # 0 3 6....
print(shoplist[::-1])