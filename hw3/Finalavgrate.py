import pandas as pd
import numpy as np
import json

def data(file_path):
    global res
    tmp = pd.read_csv(file_path)
    A=tmp
    A = A[['toanslinesavg','uploadavg','answer_rateavg','final_score','first_score','total_time','timeavg','average_change']].values
    if len(A)>0:
        A[:, 0] = dataDirection_1(A[:, 0])
        A[:, 1] = dataDirection_3(A[:, 1], 1, 5)
        A[:, 5] = dataDirection_1(A[:, 5])
        A[:, 6] = dataDirection_1(A[:, 6])
        # 使可能为负的平均分数变化变为正
        A[:, 7] = A[:, 7] + 100
        A = standard(A)
        rate = Topsis(A)
        res = tmp[["case_id", "type"]].reset_index(drop=True).join(pd.DataFrame({'rate': rate}))
    return res

# 极小型指标 -> 极大型指标
def dataDirection_1(datas):
    return np.max(datas) - datas


# 中间型指标 -> 极大型指标
def dataDirection_2(datas, x_best):
    temp_datas = datas - x_best
    M = np.max(abs(temp_datas))
    answer_datas = 1 - abs(datas - x_best) / M  # 套公式
    return answer_datas

# 区间型指标 -> 极大型指标
def dataDirection_3(datas, x_min, x_max):
    M = max(x_min - np.min(datas), np.max(datas) - x_max)
    answer_list = []
    for i in datas:
        if (i < x_min):
            answer_list.append(1 - (x_min - i) / M)  # 套公式
        elif (x_min <= i <= x_max):
            answer_list.append(1)
        else:
            answer_list.append(1 - (i - x_max) / M)
    return np.array(answer_list)

#正向化矩阵标准化
def standard(datas):
    s = np.power(np.sum(pow(datas, 2), axis=0), 0.5)
    for i in range(0, s.size):
        for j in range(0, datas[:,i].size):
            if s[i]!=0:
                datas[j, i] = datas[j, i] / s[i]  # 套用矩阵标准化的公式
    return datas

#TOPSIS
def Topsis(datas):
    #权重
    weight=[0.1,0.05,0.1,0.4,0.05,0.1,0.1,0.1]
    s=np.ones([datas.shape[1],datas.shape[1]],float)
    for i in range(len(s)):
        for j in range(len(s)):
            if i==j:
                s[i,j]=weight[j]
            else:
                s[i,j]=0
    Z=np.ones([datas.shape[0],datas.shape[1]],float)
    Z=np.dot(datas,s)

    Zmax=np.ones([1,datas.shape[1]],float)
    Zmin = np.ones([1, datas.shape[1]], float)
    for j in range(datas.shape[1]):
        Zmax[0,j]=max(Z[:,j])
        Zmin[0,j]=min(Z[:,j])
    C=[]
    for i in range(datas.shape[0]):
        Smax=np.sqrt(np.sum(np.square(Z[i,:]-Zmax[0,:])))
        Smin=np.sqrt(np.sum(np.square(Z[i,:]-Zmin[0,:])))
        if(Smax+Smin)!=0:
            C.append(Smin/(Smax+Smin))
        else:
            C.append(0)
    return C

finalanswer=pd.DataFrame(columns=('case_id','type','rate'))
print("正在分析题目综合代码")
tmp=data("DataavrPrepare.csv")
finalanswer=pd.concat([finalanswer,tmp])
finalanswer.to_csv('finalavgrate.csv',index=False,encoding="utf_8_sig")





