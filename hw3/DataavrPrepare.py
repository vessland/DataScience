import pandas as pd
import json

typeanalysis=pd.read_csv('TypeAnalysis.csv')
codelinesavg=pd.read_csv('codeLinesAvr.csv')
codelines=pd.read_csv('CodeLinesAnalysis.csv')
rateanalysis=pd.read_csv('rateAnalysis.csv')
scoreavg=pd.read_csv('scoreAvr.csv')
timeavg=pd.read_csv('timeAvr.csv')


f = open('test_data.json', encoding='utf-8')
res = f.read()
alldata = json.loads(res)
final=[]
for key, values in alldata.items():
    cases=values['cases']
    for case in cases:
        if case['case_id'] not in final:
            final.append(case['case_id'])
result1=[]
result2=[]
result3=[]
result4=[]
result5=[]
for target in final:
    tmp1=typeanalysis[typeanalysis.case_id==int(target)][['upload_times']].values[:,0]
    tmp2=codelines[codelines.case_id==int(target)][['answer_lines']].values[:,0]
    tmp3=rateanalysis[rateanalysis.case_id==int(target)][['answer_rate']].values[:,0]
    result1.append(sum(tmp1)/len(tmp1))
    result2.append(sum(tmp2)/len(tmp2))
    tmp3=pd.DataFrame(tmp3).fillna(0).values[:,0]
    result3.append(sum(tmp3) / len(tmp3))
    result4.append(timeavg[timeavg.case_id==int(target)]['total_time'].values[0]/(sum(tmp1)/len(tmp1)))
    result5.append(typeanalysis[typeanalysis.case_id==int(target)][['type']].values[0,0])

#case_id
newone=pd.Series(final,name='case_id')
newone=newone.to_frame()
#uploadavg
newone1=pd.Series(result1,name='uploadavg')
newone1=newone1.to_frame()
#toanslinesavg
newone2=pd.Series(result2,name='ansavg')
newone2=newone2.to_frame()
toanslinesavg=abs(codelinesavg['final_lines']-newone2['ansavg'])/newone2['ansavg']
newone2=pd.Series(toanslinesavg,name='toanslinesavg')
newone2=newone2.to_frame()
#answer_rateavg
newone3=pd.Series(result3,name='answer_rateavg')
newone3=newone3.to_frame()
#timeavg
newone4 = pd.Series(result4, name='timeavg')
newone4 = newone4.to_frame()
#type
newone5 = pd.Series(result5, name='type')
newone5 = newone5.to_frame()
answer=newone.join(newone1).join(newone5).join(newone2).join(newone3).join(scoreavg[['final_score','first_score']]).join(timeavg['total_time']).join(newone4).join(scoreavg['average_change'])

print(answer.isna().sum())
answer.to_csv('DataavrPrepare.csv',index=False,encoding="utf_8_sig")