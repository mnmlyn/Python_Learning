#coding=utf-8
# 服务端

import socket

httpheader = '''\
HTTP/1.1 302 Moved Temporarily
Server: JSP2/1.0.26
Location: '''

address = '0.0.0.0'
port = 12107

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
try:
  listener.bind((address, port))
except:
  print '[ERROR] Bind listener'

listener.listen(3)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
  server.bind(('0.0.0.0', 11129))
except:
  print '[ERROR] Bind server'

server.listen(16)

while True:
  print 'New work'

  '''
  confd,addr = server.accept()
  data = confd.recv(2048)
  if not data:
    continue
  print 'Recv:', data'''

  cli_sock = listener.accept()
  new_sock = cli_sock[0]
  sock_peer = cli_sock[1]
  print cli_sock
  print sock_peer[0]
  print sock_peer[1]

  '''
  url = 'http://%s:%s' %(sock_peer[0], sock_peer[1])
  print url
  httpdata = '%s%s' %(httpheader, url)
  print httpdata
  confd.send(httpdata)
  confd.close()'''


  #new_sock.close()