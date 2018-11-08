# python3.7
# 字符编码问题，显示，传输，存储，可能是不同的编码
# python 2.x中，字符串使用ASCII编码，要使用中文，
#     应使用u"中"这样的Unicode字符串
# python 3中，字符串默认使用Unicode编码
a = "我可以显示中文"
print(a)
# 函数ord获取字符对应的数值，函数chr获取数值对应的字符
b = ord("A")
print("字母A的ASCII编码为：",end = "")
print(b)
# 函数str将数字转为字符串，这样可以使用+号拼接字符串
print("字母A的ASCII编码为：" + str(b))
c = chr(69)
print(69,"对应的字母是"+c)
d = "中"
# ord也可以获取Unicode编码的值
e = ord(d)
print("'中'的Unicode编码为" + str(e),"十六进制为" + hex(e))
# Unicode字符的书写方式，可以直接写，反斜杠u加编码十六进制
# 这样方便输出一些特殊Unicode字符
f = "\u4e2d\u6587"
print(f)
# Unicode字符串，一个字符对应两个以上的字节
# 若要在网络上传输，或是存储，要使用字节串，方法是前边加b
g = b"abc"
print(g)
# 现在学过的字符串前边加字符的有，加r代表原始字符串，加b，
# 加u在python2中代表Unicode字符串
# ---
# 使用字符串的encode方法，将Unicode字符串转换为指定编码的字节串
# 使用字节串的decode方法，将字节串按照指定编码转换为Unicode字符串
print("'中文'的utf-8编码为：","中文".encode("utf-8"))
# 字节串的书写方式，是反斜杠x加字节值的十六进制表示
h = b"\xe4\xb8\xad\xe6\x96\x87"
print(h.decode("utf-8"))
# 解码时，decode可以传入errors="ignore"，来忽略解码时的少量错误
print(h.decode("utf-8",errors="ignore"))
# h[1] = 12，错误bytes对象不能赋值
# bytes对象中，每一个位置都是一个整形
print(hex(h[1]))
# 整形转换为其他进制表示，oct八进制，bin二进制
f = 10
print("10的十六进制，八进制，二进制分别为：",f,hex(f),oct(f),bin(f))
# 十六进制字符串转为整形，用int函数
f = int("0xf",16)
print(f)
# 使用len求字符串或字节串的长度，分别求出的是字符数和字节数
print(len("中文"),len(b"\xe4\xb8\xad\xe6\x96\x87"))
# 格式化输出，两种方式，第一种和C语言很像
# 在字符串中使用%d,%f,%s,%x等占位符，字符串后跟 % (p1,p2,...)
# 如果只有一个参数，可以省略括号
# 如果字符串中存在普通字符%，使用%%来转义表示一个%
print("%s，你好，你的成绩是%d，排名第%d" % ("李明",99,1))
print("你好，排名前%d%%" % 2)
# 格式化输出，方法二，使用format
# 使用{0},{1}等做占位符，可以使用:.1f来说明输出格式
print("上次成绩{0}，成绩提升{1:.1f}%".format(99,32.125))
