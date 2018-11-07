# python3.7
# 基本的字符串操作，基本的数据类型及其转换
# 整数
a = 99
print(a)
# /默认普通除法，整除使用//
print(5/2)
print(5//2)
# 求余
print(10%3)
# 浮点数
b = 3.14
print(b)
c = 1.23e-13
print(c)
# 字符串，字符串包含引号'和"和\时，使用反斜杠\转义
d = "Let's go!"
print(d)
e = "Liming said\"Let's go!\". The path is C:\\\\nowhere\\"
print(e)
# 字符串的第一个引号前边加r代表原始字符串
# 原始字符串中的\不用来转义，直接原样输出
# 原始字符串中不能直接写引号，要写为\"，但是会原样输出为\"
# 原始字符串的最后一个字符不能为\，可以转义写为\\，但会原样输出
f = r"a\n\a\\"
print(f)
# 因此，原始字符串的使用结论：
# -----
# 原始字符串适合没有引号"，结尾不为\的其他任何字符串的原样录入
# 若存在引号，或结尾为\，使用普通字符串和原始字符串拼接
g = "Liming said\"Let's go!\". " + r"The path is C:\\nowhere" + "\\"
print(g)
# 多行内容
# 在多行的大部分位置，可以直接写\和"，
# 使用\时，若是转义字符会被自动转换为转义字符，若不是，保持\原样
# 若在多行内容的某一行结尾使用\，则是将换行符转义，即不换行
# 多行的结尾如果是\或"，要用\转义
h = """1. Liming said"Let's go!"
2.Liming said\"Let's go!" \
  Is a new Line?no
3. Liming said"Let's go!\""""
print(h)
# 布尔值 逻辑运算
print(True and False)
print(True or False)
print(not True)


