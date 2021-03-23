import json
import pandas as pd
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
timez =[]
for i in range(len(zulip_messages)):
    timez.append(zulip_messages[i]['timestamp'])
print(timez)