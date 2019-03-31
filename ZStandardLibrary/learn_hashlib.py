# Learn hashlib


# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
    # 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
    # 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
    # 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
        # 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
        # 计算f(data)很容易，但通过digest反推data却非常困难。
        # 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示


# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
    # 完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
    # 这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
    # 并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难


# 摘要算法应用
# 摘要算法能应用到什么地方？举个常用例子：
# 任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
    #    username	     password
    #    michael	      123456
    #      bob	          abc999
    #     alice	         alice2008
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。
# 此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
    #   username	                 password
    #   michael	         e10adc3949ba59abbe56e057f20f883e
    #     bob	         878ef96e86145580c38c87f0410ad153
    #    alice	         99b1c2188db85afee403b1536010c2c9

# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。


import hashlib


# MD5值

sample_1 = hashlib.md5('how to use md5 in python by hashlib'.encode('utf-8'))
print(sample_1.hexdigest())
# >>> 69b674445d8489746e79a91e671d06b9

# 可以分段计算
sample_2 = hashlib.md5()
sample_2.update('how to use md5 in '.encode('utf-8'))
sample_2.update('python by hashlib'.encode('utf-8'))
print(sample_1.hexdigest() == sample_2.hexdigest())


# 核查一个文件
with open("./temp/structdemo2.bmp", "rb") as picture:
    content = picture.read()

picture_sample_md5 = hashlib.md5(content)
print(picture_sample_md5.hexdigest())    # >>> 46451d73cfcf81abf33c2a26d50a29b7
# 在线验证
# http://www.atool88.com/file_hash.php:
# 46451d73cfcf81abf33c2a26d50a29b7


# SHA1 值
# 调用SHA1和调用MD5完全类似
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长

with open("./temp/structdemo2.bmp", "rb") as picture:
    content = picture.read()

picture_sample_sha1 = hashlib.sha1(content)
print(picture_sample_sha1.hexdigest())   # >>>  57872b20cdacff9e591838f57f50c8c2858bb134

picture_sample_sha256 = hashlib.sha256(content)
print(picture_sample_sha256.hexdigest()) # >>> 7ac76b10bf17987ca7115fda30ae50a6386f2369a44fded720b7dae8aec610a0

picture_sample_sha512 = hashlib.sha512(content)
print(picture_sample_sha512.hexdigest()) # >>> 2ee593ba0909c7109a533cb2569370c72b5c397b3c395ee28989b83fdf2b230ee274a4e95576afdd0055d2dd1c06328b13f18500aa1cfa41948e7a3eb6fbabc2
