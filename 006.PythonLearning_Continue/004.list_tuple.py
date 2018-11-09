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




