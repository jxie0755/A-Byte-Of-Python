import re

# 正则表达式 必知必会 第二版

# 正则表达式的基本功能
    # 查找特定信息 (搜索)
    # 查找并编辑特定的信息(替换)


# 正则表达式
    # 一些用来匹配和处理文本的字符串
    # 由正则表达式语言创建, 这门语言有特殊的语法和指令
        # 不存在正则表达式程序
        # 不可以直接运行, 无法购买
        # 但是在绝大多数软件产品,编程语言,开发环境中已被实现
    # 解法不唯一
        # 有的简单
        # 有的快速
        # 有的兼容性好

# 用法
    # 大多数时候用于匹配, 但是也可以用来替换操作, 例如 将网址加厚加上HTML语言,变成可点击的链接



# 匹配纯文本
print(re.findall(r'Be', 'Ben BBe is my name'))
# >>> ['Be', 'Be']

# 用.替代任何,甚至.本身
print(re.findall(r'c.t', 'cat, cot, scut, sc@t, sc t'))
# >>> ['cat', 'cot', 'cut', 'c@t', 'c t']

# 匹配特殊字符使用转义
print(re.findall(r'c.\.t', 'cat, caat, ca.t'))
# >>> ['ca.t']
print(re.findall(r'Array\[0\]', 'Array[0]'))
# >>> ['Array[0]']

# 匹配某个字符
print(re.findall(r'[cs]at', 'cat, sat, nat')) # 规定a前面必须只能是c和s
# >>> ['cat', 'sat']

# 匹配区间
print(re.findall(r'[cs]at[0-9]', 'cat, sat11, nat')) # t之后必须接一个数字
# >>> ['sat1']

# 取非, []内用^
print(re.findall(r'[cs]at[^0-9]', 'cat, sat11, nat')) # t之后必须接一个数字
# >>> ['cat,']

# 重复匹配次数限定
print(re.findall(r'(\d{1,2}[-\/])(\d{1,2}[-\/])\d{2,4}', '4/8/03 10-6/2004 2/2/2 01-02-01'))
# >>> [('4/', '8/'), ('10-', '6/'), ('01-', '02-')]


# 判断边界,但是不包括边界
# \B 表示边界必须是空白
print(re.findall(r'[a-z]{2}', 'aa bbk kcc kddk'))
# >>> ['aa', 'bb', 'kc', 'kd', 'dk']
print(re.findall(r'\b[a-z]{2}\b', 'aa bbk kcc kddk'))
# >>> ['aa']
print(re.findall(r'[a-z]{2}\b', 'aa bbk kcc kddk'))
# >>> ['aa', 'bk', 'cc', 'dk']
print(re.findall(r'\b[a-z]{2}', 'aa bbk kcc kddk'))
# >>> ['aa', 'bb', 'kc', 'kd']

# \B 表示边界不能是空白
print(re.findall(r'\B[a-z]{2}\B', 'aa bbk kcc kddk'))
# >>> ['dd']
print(re.findall(r'[a-z]{2}\B', 'aa bbk kcc kddk'))
# >>> ['bb', 'kc', 'kd']
print(re.findall(r'\B[a-z]{2}', 'aa bbk kcc kddk'))
# >>> ['bk', 'cc', 'dd']









