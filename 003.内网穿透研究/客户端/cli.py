#coding=utf-8
# 客户端

import socket
import time

s_address = '192.168.66.190'
s_port = 12107
s_sock = (s_address, s_port)

c_address = '0.0.0.0'
c_port = 80
c_sock = (c_address, c_port)

while True:
  clifd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clifd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  #clifd.bind(c_sock)

  clifd.connect(s_sock)
  time.sleep(10)