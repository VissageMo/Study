name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "SWA"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:  # find 查找不到会返回 -1
    print('Yes, it contains the string "war"')

delimiter = '__*__'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
