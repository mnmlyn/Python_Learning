# coding=utf-8
import bjtuService
import time

def print8(str):
    print unicode(str,'utf-8')

aa = bjtuService.bjtuService('17120095','mmm1884203')

nowDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))

if aa.Login():
    print 'Login'
    result = aa.searchNetUsageDetail('2018-01-01',nowDate)
    #print result
    print8('2018-03-01到'+nowDate+'，共'+str(len(result))+'条数据')

    macUsage = {}

    for item in result:
        if macUsage.has_key(item['MAC']):
            macUsage[item['MAC']] +=  float(item['dataUsed'])
        else:
            macUsage[item['MAC']] = 0

    #print macUsage

    print8('流量统计(MAC:MB)')
    for mac in macUsage.keys():
        print mac + ":" + str(macUsage[mac])

    print8('在线列表')

    for data in aa.getOnlineClient():
        print data

    #print8('强制下线')
    #aa.forceToOffLine(mac='2082C0239FB0',ip='172.26.135.203')

else:
    print 'Login Error'

raw_input('Press <Enter>')

