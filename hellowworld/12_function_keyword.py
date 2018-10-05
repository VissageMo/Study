def func(a, b=5, c=10):
    print('a is', a, 'and b is', b,'and c is', c)

a=9

func(3,7)
func(25, c=24)
func(c=50,a=a)  # 此处全局变量和形参并不冲突
