import json
import main
import pandas as pd
from datetime import datetime
import numpy as np
import math
import matplotlib.pyplot as plt
from func import divide_chunks
my_email = 'gstsaturyan@miem.hse.ru'

with open('JitsiSession.json') as JitsiSession:
    data4 = json.load(JitsiSession)
dfjits = pd.DataFrame(data4)

my_data = dfjits[dfjits['username'] == my_email]
# Index(['_id', 'begin', 'end', 'date', 'room', 'username'], dtype='object')
begin = np.array(list(map(lambda x: int(x[:5].replace(':','')),my_data['begin'])))
end = np.array(list(map(lambda x: int(x[:5].replace(':','')),my_data['end'])))

new_array = end - begin
date  = list(my_data['date'].values)
if len(date) == len(new_array):
    dic = dict(zip(new_array,date))
else:
    print("data is not full")
dev1 = list(dic.keys())
dev2 = list(dic.values())
# print(date)
# print(new_array)
# for i in range(len(new_array)):
#     if new_array[i]<30:
ind = np.where(new_array > 30)[0].tolist()
final_dates =[]
for i in range(len(date)):
    if ind.count(i) and date[i] not in final_dates:
        final_dates.append(date[i])
# print(len(final_dates))
dev_final_dates = list(divide_chunks(final_dates,4))
