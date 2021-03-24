import json
import pandas as pd
from datetime import datetime
import numpy as np
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


dfzulip = pd.DataFrame(data1)
my_data = dfzulip[dfzulip['email'] =='vyumoiseenkov@miem.hse.ru']
zulip_messages = my_data.iloc[0]['messages'] #type - dict

dfgit = pd.DataFrame(data2)
my_data2 = dfgit[dfgit['email'] == 'vyumoiseenkov@miem.hse.ru']




timezulip =[]
# timezulip.append('2021-01-17T22:44:45')
for i in range(len(zulip_messages)):
    timezulip.append(zulip_messages[i]['timestamp'][:19].replace('T',' '))
    timezulip[i] = datetime.strptime(timezulip[i],'%Y-%m-%d %H:%M:%S' )

# timegit = []
# for j in range(len()):



# a= '2021-01-17T22:44:45'
# a = a.replace('T',' ')
# timezulip.append(datetime.strptime(a,'%Y-%m-%d %H:%M:%S'))

# print(timezulip)
# print(zulip_messages)
# print(timezulip[0].date())


new_array = list(map(lambda x: x.date().month,timezulip))
# print(new_array)

c = Counter()
for word in new_array:
    c[word]+=1
x = list(c.keys())
y =  list(c.values())
labels = ['January','February','March']
range = np.arange(1,4,1)

plt.scatter(x,y,color = 'r',label = 'Zulip')
plt.legend()
plt.xlabel('Date')
plt.xticks(np.arange(1,5,1))
plt.ylim(0,10)
plt.grid()
plt.xticks(range,labels = labels)
plt.ylabel('activity Count')
plt.show()