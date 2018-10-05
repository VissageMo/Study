import sys  # 使用import导入模块，sys为内置模块

print('The command line arguments are:')
for i in sys.argv:  # sys.argv变量是一系列字符串的列表，包含了命令行参数这一列表，也就是使用命令行传递给程序的参数
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

