# coding=utf-8
import requests
import random
import re
import hashlib

class bjtuService(object):

    def __init__(self,account='15311026',password = 'duan1883092'):
        self.cookie = self.getCookieLocal()
        self.account = account
        self.password_raw = password
        self.password = self.calMD5(password)
        self.accountInfo = {}
        self.NetUsedDetailData = []
        self.OnlineClient = []
        pass

    def calMD5(self,password_raw):
        md = hashlib.md5()
        md.update(password_raw)
        return md.hexdigest()

    def getCookieLocal(self):
        cookie_file = open('cookie.txt', 'r')
        cookie = cookie_file.read()
        cookie_file.close()
        return cookie

    def setCookieLocal(self,cookie):
        cookie_file = open('cookie.txt', 'w')
        cookie_file.write(cookie)
        cookie_file.close()
        self.cookie = cookie

    # 判断是否为登陆状态
    def isLoginState(self):
        headers = {
            'Host': 'service.bjtu.edu.cn',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://service.bjtu.edu.cn/LoginAction.action',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': self.cookie
        }
        url = 'http://service.bjtu.edu.cn/refreshaccount?t=' + str(random.random())
        r = requests.get(url, headers=headers)
        rc = r.content
        if self.account in rc:#证明当前登陆状态
            try:
                self.accountInfo = eval(rc)
            except:
                pass
            return True
        else:
            try:
                rc = rc.replace('null',"'null'")
                self.accountInfo = eval(rc)
                pass
            except:#可能是登陆了其他账号，销毁当前cookie，方便重新登陆
                self.setCookieLocal('ERROR')
                pass
            return False

    def Login(self):
        if self.isLoginState():
            return True
        url = 'http://service.bjtu.edu.cn/nav_login'
        headers = {
            'Host': 'service.bjtu.edu.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://service.bjtu.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': self.cookie
        }
        r = requests.get(url, headers=headers)
        rh = r.headers
        rc = r.content
        # 从响应头部rh中找到cookie
        pattern = re.compile(r'\s*(JSESSIONID=[0-9A-Z]*);\s*Path')
        if 'Set-Cookie' in rh.keys():
            setcookie = rh['set-cookie']
            result = pattern.findall(setcookie)
            if len(result) >= 1:
                cookie = result[0]
            else:
                cookie = 'ERROR'
            self.setCookieLocal(cookie)
        else:
            #return False # 可能服务器并没有要求设置新的cookie，而是使用客户端提交过来的cookie，这时继续登录即可
            pass

        # 获取验证码，虽然不用提交验证码，但是获取验证码是必须的，不然不能不能登录成功
        headers1 = {
            'Host': 'service.bjtu.edu.cn',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Accept': 'image/webp,image/*,*/*;q=0.8',
            'Referer': 'http://service.bjtu.edu.cn/nav_login',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': self.cookie
        }
        url1 = 'http://service.bjtu.edu.cn/RandomCodeAction.action?randomNum=' + str(random.random())
        requests.get(url1, headers=headers1)

        # 找到checkcode
        pattern = re.compile(r'var\s*checkcode="(\d{,4})";')
        result = pattern.findall(rc)
        if len(result) >= 1:
            checkcode = result[0]
        else:
            return False

        # 提交登录信息
        headers['Referer'] = 'http://service.bjtu.edu.cn/nav_login'
        headers['Origin'] = 'http://service.bjtu.edu.cn'
        headers['Cache-Control'] = 'max-age=0'
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Accept-Encoding'] = 'gzip, deflate'
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        headers['Cookie'] = self.cookie
        post_data = {
            'account': self.account,
            'password': self.password,
            'code': '',
            'checkcode': checkcode,
            'Submit': '登 录',
        }
        url = 'http://service.bjtu.edu.cn/LoginAction.action'
        res1 = requests.post(url, headers=headers, data=post_data)

        return self.isLoginState()
        pass

    def searchNetUsageDetail(self,startDate='2017-07-01',endDate='2017-07-02'):
        headers = {
            'Host': 'service.bjtu.edu.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://service.bjtu.edu.cn/nav_loginLog',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control' : 'max-age=0',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Origin' : 'http://service.bjtu.edu.cn',
            'Cookie': self.cookie
        }
        url = 'http://service.bjtu.edu.cn/UserLoginLogAction.action'
        post_data = {
            'type': '4',
            'startDate': startDate,
            'endDate': endDate
        }
        r = requests.post(url, headers=headers, data=post_data)
        rc = r.content
        try:
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
                                  )''', re.DOTALL | re.X)
            result = pattern.findall(rc)
            self.NetUsedDetailData = []
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

                self.NetUsedDetailData.append(rowdataDict)
            return self.NetUsedDetailData
        except:
            return {}

    def getOnlineClient(self):
        url = "http://service.bjtu.edu.cn/nav_offLine?t=" + str(random.random())
        headers = {
            'cookie' : self.cookie
        }
        r = requests.get(url,headers=headers)
        rc = r.content
        # 正则匹配找到在线账号信息
        pattern = re.compile(r'''
            (?:<tr>\s*
                <td>\s*
                ((?:19|20)\d{2}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12][0-9]|3[01])\s+(?:0?[0-9]|1[0-9]|2[0-3])(?::[0-5][0-9]){2}) #日期 时间
                \s*&nbsp;\s*</td>\s*
                <td>\s*
                ((?:(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])) #IP地址
                \s*&nbsp;\s*</td>\s*
                <td>.*?</td>\s* # .*是贪婪的，在其后加上?变为.*?，则为非贪婪匹配
                <td>\s*
                ([\dA-Z]{12}) # MAC地址
                \s*&nbsp;\s*</td>\s*
                <td.*?>\s*(\d+)\s*</td>\s* # 匹配隐藏的标识号Tag
                (?:<td.*?/td>\s*) # 非贪婪匹配<td>标识
                .*?
            </tr>)
        ''',re.DOTALL | re.X)
        result = pattern.findall(rc)
        self.OnlineClient = []
        for rowdata in result:
            rowdict = {}
            rowdict['LoginTime'] = rowdata[0]
            rowdict['IP'] = rowdata[1]
            rowdict['MAC'] = rowdata[2]
            rowdict['Tag'] = rowdata[3]
            self.OnlineClient.append(rowdict)
        return self.OnlineClient

    # mac,ip,tag三个条件满足其一，则强制下线。对于tag不做验证，尽量不用
    def forceToOffLine(self,mac="",ip="",tag=""):
        tags = []
        tag = tag.strip()
        if tag != "":
            tags.append(tag)
            print 'add Tag ' + tag
        for rowdata in self.OnlineClient:
            if rowdata['IP'] == ip or rowdata['MAC'] == mac:
                if rowdata['Tag'] not in tags:
                    tags.append(rowdata['Tag'])
                    print 'add Tag for IP or MAC ' + rowdata['Tag']

        headers = {
            'cookie': self.cookie
        }
        for onetag in tags:
            url = "http://service.bjtu.edu.cn/tooffline?t=" + str(random.random()) + "&fldsessionid=" + onetag
            requests.get(url,headers=headers)


