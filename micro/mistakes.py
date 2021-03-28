import json
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import main
from func import get_zulip_info
from collections import Counter

with open('JitsiSession.json') as JitsiSession:
    data4 = json.load(JitsiSession)
dfjitsi = pd.DataFrame(data4)
# my_data4 = dfjitsi[dfjitsi['email'] == 'vyumoiseenkov@miem.hse.ru']
# print(my_data4.iloc[0])
# def accountexist(array) -> bool:
# print(my_data2['projects'].iloc[0])

mydate = dfjitsi[dfjitsi['username'] == 'kamedvedev@miem.hse.ru']

begin = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['begin'])))
end = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['end'])))

for_sec_array = end - begin

for_sec_array = for_sec_array[for_sec_array > 40]
yjits = [len(for_sec_array[:4]),len(for_sec_array[4:8]),len(for_sec_array[8:])]
my_email = 'vyumoiseenkov@miem.hse.ru'


# a = get_zulip_info('ZulipStats.json',my_email)
# object = main.Zulip(list(a[1]),list(a[0]),my_email)
# # print(object.message(),object.months())
# # b = main.Plot(object.months(),object.message())
# b.plotting("g","zulip")
# plt.show()
with open('GitStats2.json') as git:
    dfgit = pd.DataFrame(json.load(git))
myd = dfgit[dfgit['email'] == 'vyumoiseenkov@miem.hse.ru']
# print(myd['commits_stats'].tolist()[0])
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]
commitsum = 0
a =myd['commits_stats'].tolist()[0]
arData =[]
arCommit =[]
for i in range(len(a)):
    commitsum += a[i]['commitCount']
    arData.append(a[i]['beginDate'][4:7])
    arCommit.append(a[i]['commitCount'])
# arData.append('Mar')
# arCommit.append('4')
# print(arData)
# print(arCommit)
# for i in range(len(arData)-1):
#     if arData[i] == arData[i+1]:
a = [0,1,0,0]
print(a.count(a==0))
print(type(a))
# print(commitsum)
print(10.5 % 10)
