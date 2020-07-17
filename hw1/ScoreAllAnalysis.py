import json
import os
import xlwt

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"each_score")
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
        if(len(uploads)>0):
            for j in range(0, len(uploads)):
                score=uploads[j]['score']
                worksheet.write(i,2+j,score)
        i=i+1
workbook.save('ScoreAllAnalysis.xls')