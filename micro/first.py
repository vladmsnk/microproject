import json
import pandas as pd
from datetime import datetime
import numpy as np
import math

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

# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def retlen(lst):
    a =[]
    for i in range(len(lst)):
        a.append(len(lst[i]))
    return a
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

c = Counter()
for word in new_array:
    c[word]+=1
x = list(c.keys())
y =  list(c.values())
labels = ['January','February','March']
rang = np.arange(1,4,1)

# jitsi
dfjitsi = pd.DataFrame(data4)
mydate = dfjitsi[dfjitsi['username'] == 'vyumoiseenkov@miem.hse.ru']
begin = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['begin'])))
end = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['end'])))
for_sec_array = end - begin
for_sec_array = for_sec_array[for_sec_array > 40].tolist()
new2 = list(divide_chunks(list(for_sec_array),math.ceil(len(for_sec_array)/3)))
yjits = retlen(new2)

# print(yjits)
plt.scatter(x,y,color = 'r',label = 'Zulip')
plt.scatter(rang,yjits,color ='g',label='Jitsi')
plt.legend()
plt.xlabel('Date')
plt.xticks(np.arange(1,5,1))
plt.ylim(0,10)
plt.grid()
plt.xticks(rang,labels = labels)
plt.ylabel('activity Count')
plt.show()