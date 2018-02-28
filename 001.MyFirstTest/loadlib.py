# coding=utf-8

# import mylib
#
# h = mylib.Hello()
# h.sayHello()

#下面这种方法，不用每次使用Hello类时，加mylib.,而是可以直接用
from mylib import Hello

h=Hello()
h.sayHello()
