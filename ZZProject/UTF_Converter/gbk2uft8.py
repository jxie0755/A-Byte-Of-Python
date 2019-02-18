import os
import chardet
import codecs


def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def GBK_2_UTF8(src, dst):
    #     检测编码，coding可能检测不到编码，有异常
    f = open(src, "rb")
    coding = chardet.detect(f.read())["encoding"]
    f.close()
    if coding != "utf-8":
        with codecs.open(src, "r", coding) as f:
            try:
                WriteFile(dst, f.read(), encoding="utf-8")
                try:
                    print(src + "  " + coding + " to utf-8  converted!")
                except Exception:
                    print("print error")
            except Exception:
                print(src +"  "+ coding+ "  read error")

# 把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:
          	#递归函数，遍历所有子文件夹
            ReadDirectoryFile(dirname)
        for filename in filenames:
            if filename.endswith(".java"):
                GBK_2_UTF8(os.path.join(parent, filename),
                           os.path.join(parent, filename))

if __name__ == "__main__":
    src_path = "D:\Documents\GitHub\Data_Structure_with_Java\Java_小白大牛_源代码"
    # 此处遍历路径下所有子目录
    # 把所有java文件从gbk编码改为utf-8不会破坏原信息
    ReadDirectoryFile(src_path)
