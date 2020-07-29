# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
# import docx
from hw5.recomPre import top4_similar, recommend


# 数据准备
os.chdir(r"C:\Users\昭宁\Desktop\数据科学基础大作业\DataScience\hw6")
data = pd.read_csv("Userrate2.csv")
columns = ['user_id', 'rate', '字符串', '线性表', '数组', '查找算法', '排序算法', '数字操作', '图结构', '树结构']
quantile_data = pd.read_csv("quantiles.csv")
data2 = pd.read_excel("rate_per_person_per_fact.xls")


# 根据user_id返回对应建议字符串
def make_suggestions(user_id):
    line1 = data[data.user_id == user_id]  # user_id对应的数据行
    line2 = data2[data2.user_id == user_id]
    if(line2.size== 0):
        print(user_id)
    rate = line1['rate'].values[0]
    rank = rank_of_total_rate(rate)
    types = suggestion_for_type_of_question(line1)
    code_quality = suggestion_for_code_quality(line2)

    partners = suggestion_for_partner(user_id)
    questions = suggestion_for_question(user_id)

    suggestion = '\n你的能力评分是{rate}(满分为100)，超过了{rank}的人。' + types + code_quality + partners + questions
    return suggestion.format(rate=round(rate * 100, 2), rank=rank)


# 获得总评分击败人数的百分比，返回 "xx%" 格式字符串
def rank_of_total_rate(rate):
    # 评分列表
    rates_list = np.array(data['rate']).tolist()
    rates_list.sort()

    index = rates_list.index(rate)
    return str(round(index * 100 / len(rates_list), 2)) + '%'


# 返回题型的评价
def suggestion_for_type_of_question(line):
    goods = []  # 分数高于DOOD的题型
    bads = []  # 分数低于BAD的题型
    for i in range(2, 10):
        rate = line[columns[i]].values[0]  # 某一题型的成绩
        if rate >= quantile_data.at[1,columns[i]]:
            goods.append(columns[i])
        elif rate < quantile_data.at[0,columns[i]]:
            bads.append(columns[i])

    suggestion = '与他人相比,'
    num_of_types = 8
    if len(goods) == 0 and len(bads) == 0:
        suggestion += '你对各种题型都较为熟悉，但还有提升空间，可以多些练习和参考别人的优秀代码噢！'
    elif len(bads) == 8:
        suggestion += '你对所有题型都不太熟悉，需要好好学习数据结构与算法的内容，多加练习！'
    else:
        suggestion += '你'
        if len(goods) > 0:
            suggestion += '较为擅长的题型是' + '、'.join(goods) + '，请继续保持；'
        else:
            suggestion += "没有特别擅长的题型；"
        if len(bads) > 0:
            suggestion += '较为薄弱的是' + '、'.join(bads) + "（其中可能包含你未做过的题型），需要加强。"
        else:
            suggestion += "没有特别薄弱的题型，太棒了！"
    return suggestion


# 返回代码质量的评价
def suggestion_for_code_quality(line):
    suggestion = '你的代码质量（包括注释、复杂度等）'
    if line['answer_rate'].values[0] > quantile_data.at[1,'answer_rate']:
        suggestion += '较高，请继续保持。'
    elif quantile_data.at[0,'answer_rate'] <= line['answer_rate'].values[0] < quantile_data.at[1,'answer_rate']:
        suggestion += '中等，可以学习模仿一下他人的优秀代码噢。'
    else:
        suggestion += '较差，赶紧学习一下算法和数据结构的知识以提高代码效率，并注意培养优良的代码风格噢！'
    return suggestion


# 返回推荐共同学习的伙伴
def suggestion_for_partner(user_id):
    similar_user_detail = top4_similar(str(user_id))
    similar_user_id = []
    for e in similar_user_detail:
        similar_user_id.append(e[0])
    return 'ID为' + '、'.join(similar_user_id) + '的用户与你的相似度较高，可以找到他们和他们共同进步噢！'


# 返回推荐的题目ID
def suggestion_for_question(user_id):
    questions = recommend(str(user_id))
    questions_id = []
    for e in questions:
        questions_id.append(e[0])
    return '以下是我们给你推荐的题目ID：\n' + '\t'.join(questions_id) + '\n'


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == '__main__':

    fail = open(os.getcwd() + '\\suggestions\\' + "fail.txt","w")
    fail.truncate()
    fail.close()
    fail = open(os.getcwd() + '\\suggestions\\' + "fail.txt","a")
    user_list = data['user_id'].tolist()
    for user_id in user_list:
        try:
            suggestions = make_suggestions(user_id)
            mkdir(os.getcwd() + '\\suggestions\\' + str(user_id) + '\\')
            with open(os.getcwd() + '\\suggestions\\' + str(user_id) + '\\' + str(user_id) + '_suggestion.txt', 'w') as f:
                f.write(suggestions)
            #复制图片
            f_src = open(os.getcwd() + '\\picture\\' + str(user_id) + '.png', 'rb')
            content = f_src.read()
            f_copy = open(os.getcwd() + '\\suggestions\\' + str(user_id) + '\\' + str(user_id) + '_question_type.png', 'wb')
            f_copy.write(content)
            f_src.close()
            f_copy.close()
        except Exception as e :
            fail.write(str(user_id) + '\n')
    fail.close()

    # 想要创建word文档把建议和图片放到一个文件，但docx模块用不了。暂缓
    # user_id = 39200
    # doc = docx.Document()  # 创建一个Document对象
    # doc.add_paragraph('用户'+str(user_id)+'的测评结果')  # 增加一个paragraph
    # doc.add_paragraph(suggestions)
    # # 插入照片
    # doc.add_picture(os.getcwd() + '\\picture\\' + str(user_id) + '.png', width=docx.shared.Inches(5))
    # doc.save(os.getcwd() + '\\suggestions\\' + str(user_id) + '.docx')  # 保存文档



