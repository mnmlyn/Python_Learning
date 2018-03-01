# coding=utf-8
import bjtuService

aa = bjtuService.bjtuService()

if aa.Login():
    print 'Login'
    result = aa.searchNetUsageDetail('2018-01-01','2018-03-01')
    print result
    print len(result)

    macUsage = {}

    for item in result:
        if macUsage.has_key(item['MAC']):
            macUsage[item['MAC']] +=  float(item['dataUsed'])
        else:
            macUsage[item['MAC']] = 0

    print macUsage

    for mac in macUsage.keys():
        print mac + ":" + str(macUsage[mac])

    print '在线列表'

    for data in aa.getOnlineClient():
        print data

    print '强制下线'
    aa.forceToOffLine(mac='2082C0239FB0',ip='172.26.135.203')

else:
    print 'Login Error'

