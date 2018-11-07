# python3.7
# 字符编码问题，显示，传输，存储，可能是不同的编码
# python 2.x中，字符串使用ASCII编码，要使用中文，应使用u"中"这样的Unicode字符串
# python 3中，字符串默认使用Unicode编码
a = "我可以显示中文"
print(a)
# 函数ord获取字符对应的数值，函数chr获取数值对应的字符
b = ord("A")
print("字母A的ASCII编码为：",end = "")
print(b)
print("字母A的ASCII编码为：" + str(b))# str将数字转为字符串，
                                      # 这样可以使用+号拼接字符串
c = chr(69)
print(69,"对应的字母是"+c)
# 中文编码
d = "中"
# Unicode编码  "中"  Unicode:20013  HEX:0x4e2d
e = ord(d)
print("'中'的Unicode编码为" + str(e),"十六进制为" + hex(e))