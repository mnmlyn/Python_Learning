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

else:
    print 'Login Error'

