import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

data=pd.read_csv('Userrate1.csv')

f = open('test_data.json', encoding='utf-8')
res = f.read()
alldata = json.loads(res)
final = []
for key, values in alldata.items():
    final.append(values['user_id'])
for userid in final:
    labels=['字符串','线性表','数组','查找算法','排序算法','数字操作','图结构','树结构']
    userdata=data[data.user_id==userid][['字符串','线性表','数组','查找算法','排序算法','数字操作','图结构','树结构']].values[0]*100
    angles=np.linspace(0,2*np.pi,8,endpoint=False)
    userdata = np.concatenate((userdata, [userdata[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, userdata, 'o-', linewidth=2)
    ax.fill(angles, userdata, 'r', alpha=0.5)
    ax.set_thetagrids(angles * 180 / np.pi, labels,)
    ax.set_ylim(0, 100)
    ax.grid(True)
    plt.title("userid为"+str(userid)+'用户总评分为'+str(round(data[data.user_id==userid]['rate'].values[0]*100,2)),pad=10)
    plt.savefig("picture/"+str(userid)+".png")
    plt.clf()