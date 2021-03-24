import json
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

with open('JitsiSession.json') as JitsiSession:
    data4 = json.load(JitsiSession)
dfjitsi = pd.DataFrame(data4)
# my_data4 = dfjitsi[dfjitsi['email'] == 'vyumoiseenkov@miem.hse.ru']
# print(my_data4.iloc[0])
# def accountexist(array) -> bool:
# print(my_data2['projects'].iloc[0])

mydate = dfjitsi[dfjitsi['username'] == 'vyumoiseenkov@miem.hse.ru']
# print(mydate['begin'].iloc[5],' ',mydate['end'].iloc[5])
# print(mydate['begin'],' ',mydate['end'])
begin =np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['begin'])))
end = np.array(list(map(lambda x: int(x[:5].replace(':','')),mydate['end'])))
# print(begin)
# print(end)
# print(end - begin)
for_sec_array = end - begin
# print(for_sec_array)
print(for_sec_array[for_sec_array > 30])