import json

import pandas as pd
from datetime import datetime
import numpy as np
import math
from collections import Counter
from itertools import groupby


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_zulip_info(filename:str,email: str):
    """
    :param filename: the name of file
    :param email: user's email
    :return: the list of months and corresponding activities
    """
    with open(filename) as zulip:
        datazulip = pd.DataFrame(json.load(zulip))
    my_data = datazulip[datazulip['email'] == email]
    zulip_messages = my_data.iloc[0]['messages']
    timezulip = []
    for i in range(len(zulip_messages)):
        timezulip.append(zulip_messages[i]['timestamp'][:19].replace('T', ' '))
        timezulip[i] = datetime.strptime(timezulip[i], '%Y-%m-%d %H:%M:%S')
    new_array = list(map(lambda x: x.date().month, timezulip))
    c = Counter()
    for word in new_array:
        c[word] += 1
    return (c.keys(),c.values()) # c.keys - month, c.values - activity

def get_jitsi_lecture_info(filename: str, email: str):
    with open(filename) as jitsi:
        datajitsi = pd.DataFrame(json.load(jitsi))
    my_data = datajitsi[datajitsi['username'] == email]
    begin = np.array(list(map(lambda x: int(x[:5].replace(':', '')), my_data['begin'])))
    end = np.array(list(map(lambda x: int(x[:5].replace(':', '')), my_data['end'])))
    newar = end - begin
    date = list(my_data['date'].values)
    ind = np.where(newar > 30)[0].tolist()
    final_dates = []
    for i in range(len(date)):
        if ind.count(i) and date[i] not in final_dates:
            final_dates.append(date[i])

    partdate = np.array(list(map(lambda x: int(x[5:7].replace('-', '')), my_data['date'])))
    new_x = [el for el, _ in groupby(partdate)]
    dev_final_dates = list(divide_chunks(final_dates, math.ceil(len(final_dates) / len(new_x))))
    foret = list(map(lambda x: len(x), dev_final_dates))
    return (new_x,foret)

def get_git_intfo(filename: str, email: str):
    with open(filename) as dfgit:
        myd = dfgit[dfgit['email'] == 'vyumoiseenkov@miem.hse.ru']
    a = myd['commits_stats'].tolist()[0]
    arData = []
    arCommit = []
    for i in range(len(a)):
        arData.append(a[i]['beginDate'][4:7])
        arCommit.append(a[i]['commitCount'])
    return(arCommit,list(range(1,len(arData) +1)))
def get_jitsi_poster_info(filename: str, email: str):
    pass




