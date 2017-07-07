# -*- coding: UTF-8 -*-
import math
import urllib2

url=urllib2.urlopen('http://172.18.0.5:8088/jmx?get=Hadoop:service=ResourceManager,name=RMNMInfo::LiveNodeManagers').read()
str_re = 0
str_t = 0
list = []
while str_t!= -1:
    str_t = url.find('AvailableMemoryMB',str_re)
    str_re = str_t + 30
    if str_t == -1:
        break
    num_s = str_t + 20
    num = ''
    while url[num_s] >= '0' and url[num_s] <= '9':
        num = num + url[num_s]
        num_s += 1
        num_i = math.ceil(int(num)/1024.0)
    list.append(num_i)
list.sort()
from collections import Counter
counter = Counter(list)
res = dict(counter)
sum1=0
sum2=0
sum3=0
print  "AvailableMemoery/GB         sum"
for key,value in res.items():
    print "     "+str(key)+"                    "+str(value)+"\t"
print
print  "range/GB            sum"

for key,value in res.items():
    if key >= 4.0 and key <= 8.0:
        sum1 += value
    if key >= 8.0 and key <= 12.0:
        sum2 += value
    if key >= 12.0:
        sum3 += value
print "4-8                 "+str(sum1)
print "8-12                "+str(sum2)
print "大于12               "+str(sum3)



