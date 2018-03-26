# coding=utf-8
import bjtuService
import time
import matplotlib.pyplot as plt

def print8(str):
    print unicode(str,'utf-8')

aa = bjtuService.bjtuService()

startDate = '2018-03-01'
nowDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))

if aa.Login():
    print 'Login'
    result = aa.searchNetUsageDetail(startDate,nowDate)
    #print result
    print8(startDate+'到'+nowDate+'，共'+str(len(result))+'条数据')

    macUsage = {}

    for item in result:
        if macUsage.has_key(item['MAC']):
            macUsage[item['MAC']] +=  float(item['dataUsed'])
        else:
            macUsage[item['MAC']] = float(item['dataUsed'])

    #print macUsage

    print8('流量统计(MAC:MB)')
    for mac in macUsage.keys():
        print mac + ":" + str(macUsage[mac])

    print8('在线列表')

    for data in aa.getOnlineClient():
        print data

    #print8('强制下线')
    #aa.forceToOffLine(mac='2082C0239FB0',ip='172.26.135.203')

    # 按照value对字典进行排序
    print8('流量排序')
    sortedMacUsage = sorted(macUsage.items(),key=lambda item:item[1])
    print sortedMacUsage
    name_list = []
    num_list = []
    for data in sortedMacUsage:
        name_list.append(data[0])
        num_list.append(data[1])

    plt.figure(figsize=(12, 3))
    plt.barh(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

else:
    print 'Login Error'

#raw_input('Press <Enter>')

