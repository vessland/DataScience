import pandas as pd
import json

data = pd.read_csv("Userrate.csv")
Usertotalrate = pd.DataFrame(columns=('user_id', 'rate','字符串','线性表','数组','查找算法','排序算法','数字操作','图结构','树结构'))

f = open('test_data.json', encoding='utf-8')
res = f.read()
alldata = json.loads(res)
final = []
for key, values in alldata.items():
    final.append(values['user_id'])
for userid in final:
    tmpstore=[]
    result=[]
    tmpstore.append(data[data.user_id == userid]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '字符串')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '线性表')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '数组')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '查找算法')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '排序算法')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '数字操作')]['rate'].values)
    tmpstore.append(data[(data.user_id == userid) & (data.type == '图结构')]['rate'].values)
    tmpstore.append( data[(data.user_id == userid) & (data.type == '树结构')]['rate'].values)
    for tmp in tmpstore:
        if(len(tmp)==0):
            result.append(0)
        else:
            result.append(sum(tmp)/len(tmp))
    Usertotalrate = Usertotalrate.append(
            pd.Series({'user_id': str(userid), 'rate': result[0], '字符串': result[1],'线性表':result[2],'数组':result[3],'查找算法':result[4],'排序算法':result[5],'数字操作':result[6],'图结构':result[7],'树结构':result[8]}),
            ignore_index=True)
Usertotalrate.to_csv('Userrate1.csv', index=False, encoding="utf_8_sig")
