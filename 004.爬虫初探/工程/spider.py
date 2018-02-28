#coding=utf-8
import re
import urllib
import urllib2
import requests
import cookielib
import random


cookie = 'JSESSIONID=F319030453E25BA1ED7A5C54A605AD9E'

url = 'http://service.bjtu.edu.cn/nav_login'
headers = {
'Host':'service.bjtu.edu.cn',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer': 'http://service.bjtu.edu.cn/',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': cookie
}

#req = urllib2.Request(url,headers=headers)
#req = urllib2.Request(url)
#req.add_header('Cookie','760FDE8195BD464A5785795152BB57AB')
#r = urllib2.urlopen(req)
r = requests.get(url,headers=headers)
info = r.headers
htmlstr = r.content
print type(info)
print info
print type(htmlstr)
print htmlstr

# 找到cookie
pattern = re.compile(r'\s*(JSESSIONID=[0-9A-Z]*);\s*Path')
if 'set-cookie' in info.keys():
  setcookie = info['set-cookie']
  result = pattern.findall(setcookie)
  cookie = result[0]
  print 'use new cookie--------------------------------'
  print cookie
  headers['Cookie'] = cookie
  r = requests.get(url,headers=headers)
  info = r.headers
  htmlstr = r.content

# 发送一个随机数
headers1 = {
'Host':'service.bjtu.edu.cn',
'Connection':'keep-alive',
'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
'Accept': 'image/webp,image/*,*/*;q=0.8',
'Referer': 'http://service.bjtu.edu.cn/nav_login',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': cookie
}
url1 = 'http://service.bjtu.edu.cn/nav_login/RandomCodeAction.action?randomNum=0.2509350187349078'
requests.get(url1,headers=headers1)

#找到checkcode
pattern = re.compile(r'var\s*checkcode="(\d{,4})";')
result = pattern.findall(htmlstr)
checkcode = result[0]

# 提交登录信息
headers['Referer'] = 'http://service.bjtu.edu.cn/nav_login'
headers['Origin'] = 'http://service.bjtu.edu.cn'
headers['Cache-Control'] = 'max-age=0'
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['Cookie'] = cookie
post_data = {
'account' : '15311026',
'password' : '5af8403bdf6ad0539754c7de694747a5',
'code' : '',
'checkcode' : checkcode,
'Submit' : '登 录',
}
print checkcode
print headers
url = 'http://service.bjtu.edu.cn/LoginAction.action'
res1 = requests.post(url,headers=headers,data=post_data)
print res1.content
#print res1.headers

#开始查询
post_data={
  'type':'4',
  'startDate':'2017-07-01',
  'endDate':'2017-07-31'
}
url = 'http://service.bjtu.edu.cn/UserLoginLogAction.action'
headers['Referer'] = 'http://service.bjtu.edu.cn/nav_loginLog'
res1 = requests.post(url,headers=headers,data=post_data)
print res1.content



#opener = urllib2.build_opener()  # 创建一个功能强大的opener
#opener.addheaders.append(('Cookie','JSESSIONID=760FDE8195BD464A5785795152BB57AB'))
#f = opener.open()
#htmlfile1 = f.read()
#print f.info()





#-----------------------------
NetUsedDetailData = []


#htmlfile = open('data.html')
try:
  #htmlstr = htmlfile.read()
  htmlstr = res1.content


  #pattern方式
  # re.DOTALL使得.(点)能够匹配换行符\n
  # re.X使得正则表达式可以写为多行，可以加入注释，且将会忽略空白
  pattern = re.compile(r'''(
                        \<tr\>
                            #\s*\<td\>(.*?)\</td\># 日期1 #这样写出了问题，中间的(.*?匹配了很多不相关的东西)
                            \s*\<td\>\s*((?:19|20)\d{2}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2]\d|3[01])#日期-年月日
                            \s+(?:(?:0?|1)\d|2[0-3]):[0-5]\d:[0-5]\d)\s*\</td\># 日期-时间 # 符号-在中括号中需要用反斜杠
                            \s*\<td\>\s*((?:19|20)\d{2}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2]\d|3[01])#日期-年月日
                            \s+(?:(?:0?|1)\d|2[0-3]):[0-5]\d:[0-5]\d)\s*\</td\># 日期-时间 # 符号-在中括号中需要用反斜杠
                            \s*\<td\s+class="number"\s+align="right"\>\s*(\d*)\s*\</td\># 使用时长3 #双引号在正则表达式中不用反斜杠
                            \s*\<td\s+class="number"\s+align="right"\>\s*(\d+\.\d+)\s*\</td\># 使用流量4 #前后都有空格，匹配中也可能有空格时，前后用空白匹配，中间的匹配用非贪婪模式(?)
                            \s*\<td\s+class="number"\s+align="right"\>\s*(\d+\.\d+)\s*\</td\># 计费金额5
                            \s*\<td\>\s*((?:(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))\s*\</td\># 登录IP
                            \s*\<td\>\s*([\dA-Z]{12})\s*\</td\># MAC
                            \s*\<td\>\s*((?:(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))\s*\</td\># NASIP
                            \s*\<td\>\s*(\d+)\s*\</td\># NASPORT
                            .*?
                        \</tr\>
                        )''',re.DOTALL|re.X)
  result = pattern.findall(htmlstr)

  for rowdata in result:
    if len(rowdata) != 10:
      continue
    rowdataDict = {}
    rowdataDict['logInDate'] = rowdata[1]
    rowdataDict['logOutDate'] = rowdata[2]
    rowdataDict['timeUsed'] = rowdata[3]
    rowdataDict['dataUsed'] = rowdata[4]
    rowdataDict['moneyUsed'] = rowdata[5]
    rowdataDict['IP'] = rowdata[6]
    rowdataDict['MAC'] = rowdata[7]
    rowdataDict['NASIP'] = rowdata[8]
    rowdataDict['NASPORT'] = rowdata[9]

    NetUsedDetailData.append(rowdataDict)

  print len(NetUsedDetailData)
  for rowdata in NetUsedDetailData:
    print rowdata
    pass
  print len(NetUsedDetailData)
  #print re.findall(r'\<tr\>.*\</tr\>', htmlstr)

finally:
  pass
  #htmlfile.close()


