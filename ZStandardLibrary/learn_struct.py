"""
Learn struct
https://docs.python.org/3/library/struct.html?highlight=struct#module-struct

准确地讲，Python没有专门处理字节的数据类型。但由于b"str"可以表示字节
所以，字节数组＝二进制str
而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换
"""


# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)
# >>> b"\x00\x9c@c"

# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes

import struct
print(struct.pack(">I", 10240099))
# pack的第一个参数是处理指令，">I"的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致
# >>> b"\x00\x9c@c")

print(struct.unpack(">IH", b"\xf0\xf0\xf0\xf0\x80\x80"))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
# >>> (4042322160, 32896)

# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了

# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
    # 两个字节："BM"表示Windows位图，"BA"表示OS/2位图；
    # 一个4字节整数：表示位图大小；
    # 一个4字节整数：保留位，始终为0；
    # 一个4字节整数：实际图像的偏移量；
    # 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度；
    # 一个4字节整数：图像高度；
    # 一个2字节整数：始终为1；
    # 一个2字节整数：颜色数。

# 所以，组合起来用unpack读取一个bmp文件：structdemo2.bmp保存为256色, 也就是8位.
with open("./temp/structdemo2.bmp", "rb") as sob:  #
    content = sob.read()[:30]
    print(content)

print(struct.unpack("<ccIIIIIIHH", content))
# >>> (b"B", b"M", 2359350, 0, 54, 40, 1024, 768, 1, 8)
# 结果显示:
# 前两位 b"B"、b"M"说明是Windows位图
# 位图大小为787510 bytes
# 分辨率为1024*768
# 颜色数为8位
