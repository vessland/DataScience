import json
import os
import xlwt

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"final_score")
worksheet.write(0,3,"first_score")
worksheet.write(0,4,"each_change")
f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
i=1
for key, values in data.items():
    cases = values['cases']
    for case in cases:
        uploads=case["upload_records"]
        worksheet.write(i,0,values['user_id'])
        worksheet.write(i,1,case['case_id'])
        worksheet.write(i,2, case['final_score'])
        if(len(uploads)>0):
            prescore = uploads[0]['score']
            worksheet.write(i, 3, prescore)
            for j in range(1, len(uploads)):
                nowscore=uploads[j]['score']
                worksheet.write(i,3+j,nowscore-prescore)
                prescore=nowscore
        i=i+1
workbook.save('ScoreAnalysis.xls')