import json
import os
import xlwt

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"total_time")
worksheet.write(0,3,"each_time")
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
            worksheet.write(i,2,uploads[len(uploads) - 1]['upload_time']-uploads[0]['upload_time'])
            pretime = uploads[0]['upload_time']
            for j in range(1, len(uploads)):
                nowtime=uploads[j]['upload_time']
                worksheet.write(i,2+j,nowtime-pretime)
                pretime=nowtime
        else:
            worksheet.write(i, 2, -1)
        i=i+1
workbook.save('TimeAnalysis.xls')