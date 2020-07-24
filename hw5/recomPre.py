import os
os.chdir(r"C:\Users\DELL\PycharmProjects\DataScience\hw5")
import pandas as pd
import numpy as np
csv_data = pd.read_csv("./finalrate.csv")

file = open("./finalrate.csv", 'r', encoding = 'UTF-8')
ratings = {} ##存放每个用户的题目和评分
for line in file.readlines()[1:50000]:
    line = line.strip().split(',')
    #如果字典中没有某位用户，则使用用户ID来创建该用户
    if not line[0] in ratings.keys():
        ratings[line[0]] = {line[3]:line[1]}
    #否则直接添加以该用户ID为key字典中
    else:
        ratings[line[0]][line[3]] = line[1]
#ratings

"""计算任何两位用户之间的相似度，由于每位用户做的题目不完全一样，所以兽先要找到两位用户共同做过的题目
       然后计算两者之间的欧式距离，最后算出两者之间的相似度
"""
from math import *
def Euclidean(user1, user2):
    #取出两个用户做过的题目和评分
    user1_rating = ratings[user1]
    user2_rating = ratings[user2]
    distance = 0
    #找到两个用户都做过的题目，并计算欧氏距离
    for key in user1_rating.keys():
        if key in user2_rating.keys():
            distance += pow(float(user1_rating[key])-float(user2_rating[key]), 2)##distance越大表示两者越相似
    return 1/(1+sqrt(distance))##返回值越小,相似度越大

"""计算某个用户和其他用户的相似度
"""
def top10_similar(userID):
    res = []
    for userid in ratings.keys():
        if not userid == userID:
            similar = Euclidean(userid, userID)
            res.append((userid, similar))
    res.sort(key = lambda val:val[1])
    return res[:4]
RES = top10_similar('48117')
#RES

"""根据用户推荐题目给其他人
"""
def recommend(user):
    #相似度最高的用户
    top_sim_user = top10_similar(user)[0][0]
    #相似度最高的用户的做题记录
    items = ratings[top_sim_user]
    recommendations = []
    #筛选出该用户未做的题目并添加到列表中
    for item in items.keys():
        if item not in ratings[user].keys():
            recommendations.append((item, items[item]))
    recommendations.sort(key = lambda val:val[1], reverse = True)#按照评分排序
    #返回评分最高的10条题目
    return recommendations[:10]
Recommendations = recommend('48117')
#Recommendations

"""计算两个用户的Pearson相关系数
"""
def pearson_sim(user1, user2):
    #取出两个用户做过的题目和评分
    user1_rating = ratings[user1]
    user2_rating = ratings[user2]
    distance = 0
    common = {}
    #找出两个用户都做过的题目
    for key in user1_rating.keys():
        if key in user2_rating.keys():
            common[key] = 1
    if len(common) == 0:
        return 0
    n = len(common)#共同题目数目
    print(n,common)
    #计算评分和
    sum1 = sum([float(user1_rating[rating]) for rating in common])
    sum2 = sum([float(user2_rating[rating]) for rating in common])
    #计算评分平方和
    sum1Sq = sum([pow(float(user1_rating[rating]),2) for rating in common])
    sum2Sq = sum([pow(float(user2_rating[rating]),2) for rating in common])
    #计算乘积和
    Psum = sum([float(user1_rating[rating]) * float(user2_rating[rating]) for rating in common])
    #计算相关系数
    num = Psum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r
R = pearson_sim('49405', '60690')
#R