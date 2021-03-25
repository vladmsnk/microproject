import json
import pandas as pd
from datetime import datetime
import numpy as np
import pprint

import matplotlib.pyplot as plt

from collections import Counter


with open('ZulipStats.json') as zulip:
    data1 = json.load(zulip)
with open('GitStats.json') as Git:
    data2 = json.load(Git)
with open('JitsiClasses.json') as JitsiClasses:
    data3 = json.load(JitsiClasses)
with open('JitsiSession.json') as JitsiSession:
    data4 = json.load(JitsiSession)

# zulip
dfzulip = pd.DataFrame(data1)
my_data = dfzulip[dfzulip['email'] =='vyumoiseenkov@miem.hse.ru']
zulip_messages = my_data.iloc[0]['messages'] #type - dict

dfgit = pd.DataFrame(data2)
my_data2 = dfgit[dfgit['email'] == 'vyumoiseenkov@miem.hse.ru']
timezulip =[]
for i in range(len(zulip_messages)):
    timezulip.append(zulip_messages[i]['timestamp'][:19].replace('T',' '))
    timezulip[i] = datetime.strptime(timezulip[i],'%Y-%m-%d %H:%M:%S' )

new_array = list(map(lambda x: x.date().month,timezulip))

# timezulip.append('2021-01-17T22:44:45')
# timegit = []
# for j in range(len()):
# a= '2021-01-17T22:44:45'
# a = a.replace('T',' ')
# timezulip.append(datetime.strptime(a,'%Y-%m-%d %H:%M:%S'))
# print(timezulip)
# print(zulip_messages)
# print(timezulip[0].date())
# print(new_array)

c = Counter()
for word in new_array:
    c[word]+=1
x = list(c.keys())
y =  list(c.values())
labels = ['January','February','March']
range = np.arange(1,4,1)

# jitsi
dfjitsi = pd.DataFrame(data4)
mydate = dfjitsi[dfjitsi['username'] == 'vyumoiseenkov@miem.hse.ru']
begin = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['begin'])))
end = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['end'])))
for_sec_array = end - begin
for_sec_array = for_sec_array[for_sec_array > 40].tolist()
print(type(for_sec_array))
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
# print(len(for_sec_array) / 3)
# yjits = [len(for_sec_array[:4]),len(for_sec_array[4:8]),len(for_sec_array[8:])]
# def chunks(lst, n):
#     a = [lst[i:i + n] for i in range(0, len(lst), n)]
#     return a
a = [1,23,4,5,6,8,9,3,1,4,5,14,5,23,4,5,1,4]
def splt(lst,n):
    yield [lst[i:i + n] for i in range(0, len(lst), n)]
def splt(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))
print(list(splt(a,3)))

# pprint.pprint(list(chunks(for_sec_array,3)))
# plt.scatter(x,y,color = 'r',label = 'Zulip')
# plt.legend()
# plt.xlabel('Date')
# plt.xticks(np.arange(1,5,1))
# plt.ylim(0,10)
# plt.grid()
# plt.xticks(range,labels = labels)
# plt.ylabel('activity Count')
# plt.show()