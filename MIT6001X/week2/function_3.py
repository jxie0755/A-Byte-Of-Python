def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)
# f(5), 重新定义x=1, 然后x+1=2
# 所以函数输出就是2
# 但是本身的print(x)依然输出5,因为x=2在函数内,不能影响函数外


def g(y):
    print(x)
    print(x + 1)

n = 5
g(x)
print(x)
# g(5)首先寻找x,发现函数内没有,所以找函数外发现x=5
# 函数输出5和6
# print(x)依然不受函数影响还是输出5


def h(y):
    x = x + 1

x = 5
h(x)
print(x)
# h(5)报错, 同样是找不到函数内的x,继而使用函数外的x=5
# 然而,函数内将改变x的赋值,这是不允许的,因为函数内无法改变函数外的全局x的赋值
