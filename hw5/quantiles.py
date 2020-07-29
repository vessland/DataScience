# -*- coding: utf-8 -*-
import pandas as pd
import xlrd

# 等级分数段定义，分位数
GOOD = 0.667  # 优
BAD = 0.333  # 良

data1 = pd.read_csv("Userrate2.csv")
columns1 = ['user_id', 'rate', '字符串', '线性表', '数组', '查找算法', '排序算法', '数字操作', '图结构', '树结构']
data2 = pd.read_excel(r"./rate_per_person_per_fact.xls")
columns2 = ['user_id', 'toanslines', 'upload_times', 'answer_rate', 'final_score', 'first_score', 'total_time', 'timeavg', 'scoreavg']


#生成分位数文件
quantiled = data1[columns1[1:]].quantile([BAD,GOOD])
quantiled.index = ['bad','good']
tmp = data2[columns2[1:]].quantile([BAD,GOOD])
tmp.index = ['bad','good']

result = pd.concat([quantiled,tmp],axis=1,join='inner')

result.to_csv('quantiles.csv',encoding="utf_8_sig")