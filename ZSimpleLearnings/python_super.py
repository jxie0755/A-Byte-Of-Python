# super主要用于继承时,不写父类名称,这样父类被改变时,减少代码改动

# 经典方式
class A():
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)  # 经典方式直接call父类A的init方法
        print('B')

class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C')

bb = B()
# >>>
# A  # 来自继承A类init的print
# B  # 来自B类init的print

cc = C()
# >>>
# A  # 来自继承A类init的print
# A  # 来自继承B类中的init的A.init的print
# B  # 来自继承B类中的print
# C  # 来自C类中的init的print

# 采用新式类，要求最顶层的父类一定要继承于object，这样就可以利用super()函数来调用父类的init()等函数
print()
class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(B, A):
    def __init__(self):
        # A.__init__(self)  # 只有补一个A类的init在前面才可以跟上例相同输出结果
        super().__init__()  # 只会寻求第一个父类,这里也就是B类
        print('C')

# 采用super()方式时，会自动找到第一个多继承中的第一个父类
bb = B()
# >>>
# A  # 来自继承A类init的print
# B  # 来自B类init的print

cc = C()
# >>>
# A  # 比之前少一个A,因为super()函数只继承第一个父类B,A的init被略过
# B  # 来自继承B类中的print
# C  # 来自C类中的init的print



# Another example
print()
class Person(object):
    def show_my_power(self):
        print("I am a person, I can walk!")

class Singer(Person):
    def show_my_power(self):
        super().show_my_power()
        print("I am a singer, I can sing!")

class Actor(Person):
    def show_my_power(self):
        super().show_my_power()
        print("I am an actor, I can act!")

class Artist(Singer, Actor):
    pass

if __name__ == "__main__":
    a = Artist()
    a.show_my_power()

# >>>
# I am a person, I can walk !
# I am an actor, I can act !
# I am a singer, I can sing !

# 注意顺序问题,竟然是先出最高父类,再出第二父类,顺序逆向
# 不同于特殊方法init, 这里的show_my_power将展示所有父类的方法,而不是只输出第一顺序父类
# 如果Singer和Actor不用super语句,那么只会输出Singer的show_my_power(第一顺序父类)
