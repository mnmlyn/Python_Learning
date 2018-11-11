# python3.7
# 列表list和元组tuple
a = ["li","zhao","wang",188]
# 方括号括起来是list，可以存放不同类型，可以直接打印list
print(a)
# len得到list中的元素个数，len也可以求字符串，字节串b"..."的长度
b = len(a)
print(b)
print(a[0])
# 索引-1代表最后一个元素
print(a[-1])
print(a[-2])
# append，添加元素到末尾
a.append("sun")
print(a)
# insert，指定位置插入指定元素
a.insert(1,"fu")
print(a)
# pop，删除指定索引（默认-1）的元素，并返回删除的元素
c = a.pop(-2)
print(a)
print(c)
d = a.pop()
print(a)
print(d)
# extend，拼接另一list
e = ["abc","def"]
a.extend(e)
print(a)
a.append(e)
print(a)
a.pop()
print(a)
# 可以对list的元素赋值，注意字符串不嫩给指定位置赋值
a[1] = "jia"
print(a)
# 元组tuple，用小括号
print("元组tuple")
f=()
print(f)
g=(1,6,7)
print(g)
# 只有一个元素的元组应该写为(1,)形式
h=(3,)
print(h)
# 若写为(1)形式，定义的不是tuple，而是一个单个变量
i=(3)
print(i)
# tuple中的元素数量和类型不能改变
# 但若tuple中包含一个可变对象，则不能修改为包含另一个可变对象，
# 却可以修改这个可变对象
# g[0]=2 # tuple对象不支持对item赋值
j=(1,2,[8,8])
print(j)
j[2][1]=9
print(j)
