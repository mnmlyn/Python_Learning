# python3.7
# 判断，循环
age=int(input("请输入年龄："))
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
# for循环，for xxx in list形式，list只要为可迭代对象即可，比如list,tuple
L = ["zhao","qian","sun","li"]
for x in L:
    print(x)
# 使用range定义范围
sum=0
for x in range(1,101):
    sum += x
print(sum)
# 使用list函数，将range转换为list
a = list(range(5))
print(a)
# while循环
n = 10
while n > 0:
    print(n // 2)
    n //= 2
# 循环中可以使用break和continue
