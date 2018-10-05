# format用来调用某些特定格式的字符串，{}中的数字可以省略


age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))  # 注意是点不是逗号
print('Why is {0} playing with that python?'.format(name))

# print默认在文字结束后进入下一行，可以在结尾出设置end来更改
print('a',end='')
print('b')

# 还可以用end指定空格结尾
print('a',end=' ')
print('b',end=' ')
print('c')

# \ 作为转义符，可以和单引号一起使用，防止该引号作为字符结束
print('what\'s your name?')
print("  \" ")

# \n 可以用来进行换行
print('This is the first line\nThis is the second one')