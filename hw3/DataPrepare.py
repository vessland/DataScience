import pandas as pd

codelines=pd.read_csv('CodeLinesAnalysis.csv')
typeanalysis=pd.read_csv('TypeAnalysis.csv')
rateanalysis=pd.read_csv('rateAnalysis.csv')
scoreanalysis=pd.read_csv('ScoreAnalysis.csv')
timeanalysis=pd.read_csv('TimeAnalysis.csv')

# 去除answer_lines为0的行
codelines=codelines.drop((codelines[codelines.answer_lines==0]).index)

#计算与标答所差行数与标答行数的比例
toanslines=abs(codelines['answer_lines']-codelines['final_lines'])/codelines['answer_lines']
newlines=pd.Series(toanslines,name='toanslines')
newlines=newlines.to_frame()
result1=codelines[['user_id','case_id']].join(newlines)
# print(result1)
result2=pd.merge(result1,typeanalysis,how="inner",on=["user_id","case_id"])
# print(result2)
# result2=result2.drop((result2[result2.upload_times==0]).index)
result3=pd.merge(result2,rateanalysis,how="inner",on=["user_id","case_id"])

result4=pd.merge(result3,scoreanalysis[['user_id','case_id','final_score','first_score']],how="inner",on=["user_id","case_id"])

result5=pd.merge(result4,timeanalysis[['user_id','case_id','total_time']],how="inner",on=["user_id","case_id"])

timeavg=abs(result5['total_time']/result5['upload_times'])
timeavgdf=pd.Series(timeavg,name='timeavg')
result6=result5.join(timeavgdf)


scoreavg=(result5['final_score']-result5['first_score'])/result5['upload_times']
scoreavgdf=pd.Series(scoreavg,name='scoreavg')
result7=result6.join(scoreavgdf)

#判断是否有空值
print(result7.isna().sum())
#去除重复项
result7.drop_duplicates()
#存入csv文件
result7.to_csv('DataPrepare.csv',index=False,encoding="utf_8_sig")