# python3.7
# 字典dict和set
# 用大括号{}括起来是字典，存储键值对
a = {"zhang":19,"li":18,"wang":20,"zhao":19}
print(a)
# 向字典新添键值对，由键得到值
a["qian"] = 22
print(a)
print(a["qian"])
# 确定键是否存在，两种方法
# 方法1：使用in，返回bool类型
print("qian" in a)
print("Tom" in a)
# 方法2：使用get，若存在返回value，否则返回None或第二个参数指定的值
print(a.get("qian"))
print(a.get("Tom"))
print(a.get("Tom",-1))
print(a.get("Tom") == None)
# 使用pop删除dict中指定key的元素
a.pop("qian")
print(a)
# 注意dict的key必须为不可变对象，比如不能用list当做key
# ---
# set可以提供元素的去重，可以放入不可变对象
# 用set(list)来将list转换为set，并且自动去掉重复元素
b = set([1,2,3,3,4,4,4,5])
c = set([4,4,4,4,5,5,6,7])
# 可以看到打印出的set，与dict一样使用大括号，
# 可以理解set是没有value的特殊dict
print(b)
print(c)
# 使用&和|可以对set求交集和并集
print(b & c)
print(b | c)
# add向set中添加元素，remove移除set中的元素
b.add(0)
print(b)
b.remove(0)
print(b)
