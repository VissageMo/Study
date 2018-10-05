shoplist = ['apple', 'mango', 'carrot', 'banana']
count = ['first', 'second', 'third', 'forth', 'last']

print('I have', len(shoplist), 'item to pruchase')

print('These times are:', end=' ')  # 为了防止换行，用 end=‘ ’ 来将末尾替换为一个空格
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')  # append 函数用来给 list 添加一个元素
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()  # sort 函数对列表进行排序
print('Sorter shopping list is', shoplist)

for i in range(0,5):
    print('THe', count[i], 'item I will buy is ', shoplist[0])
    olditem = shoplist[0]
    del shoplist[0]
    print('I bought the', olditem)
    print('Remain shopping list is', shoplist)
