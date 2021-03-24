import json
import pandas as pd
from datetime import datetime


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

timezulip =[]

for i in range(len(zulip_messages)):
    timezulip.append(zulip_messages[i]['timestamp'][:19].replace('T',' '))
    timezulip[i] = datetime.strptime(timezulip[i],'%Y-%m-%d %H:%M:%S' )
# for i in range(len(timez))
# date_time_obj = datetime.strptime(timez[0],'%Y-%m-%d')
# print(timezulip)
# print(zulip_messages)
print(type(timezulip[0]))