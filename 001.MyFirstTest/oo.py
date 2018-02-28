# coding=utf-8
# 类
class Hello:

    # 构造方法
    def __init__(self,name):
        self._name=name

    # 方法
    def sayHello(self):
        print("Hello {0}".format(self._name))

#继承
#继承自Hello
class Hi(Hello):

    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print("Hi {0}".format(self._name))


# 创建hello类的实例
h=Hello("zhangsan")
h.sayHello()

h1=Hi("jikexueyuan")
h1.sayHi()