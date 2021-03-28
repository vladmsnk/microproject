import main
from func import divide_chunks,get_jitsi_lecture_info,get_zulip_info,get_git_info,get_grade
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

my_email = 'vyumoiseenkov@miem.hse.ru'
temp1 = get_zulip_info('ZulipStats.json',my_email)
zlp = main.Zulip(temp1[1],temp1[0],my_email) #object of a Zulip class
temp2 = get_jitsi_lecture_info('JitsiSession.json',my_email)
jts = main.Jitsi(temp2[1],temp2[0],my_email)
temp3 = get_git_info('GitStats2.json',my_email)
gt = main.Git(temp3[1],temp3[0],my_email)

plot1 = main.Plot(zlp.months(),zlp.message())
plot2 = main.Plot(jts.months(),jts.lesson())
plot3 = main.Plot(gt.months(),gt.commit())
plot1.plotting('g','zulip(messages)')
plot2.plotting('r','jitsi(lectures)')
plot3.plotting('b','git(commits)')
plt.xlim(0,5)
plt.xlabel('Month')
plt.ylabel('Activity')
labels = ['Jan','Feb','Mar','Apr']
plt.xticks(list(range(1,5)),labels = labels)
plt.legend()
plt.title('График зависимости активности от времени')
plt.savefig('final.png')
plt.show()
grade = get_grade(int(zlp.exist()),int(gt.madecommit()),int(gt.exist()),int(zlp.madepost()),np.array(jts.lesson()).sum())
with open('final.html','w') as html:
    html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>График</title>
</head>
<body>
    <p><img src='final.png'></p>
    <h1 style ="text-align: center;">Current grade: {grade}</h1
</body>
</html>
""")
# print(grade)