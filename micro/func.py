import json
import pandas as pd
from datetime import datetime
import numpy as np
import math
from collections import Counter




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
    return (c.keys(),c.values()) # x,y

def get_git_intfo(filename: str, email: str):
    pass

def get_jitsi_session_info(filename: str, email: str):
    pass

def get_jitsi_classes_info(filename: str, email: str):
    pass
