import json
import xlwt

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"type")
worksheet.write(0,3,"upload_times")
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
        worksheet.write(i,2,case['case_type'])
        worksheet.write(i,3,len(uploads))
        i=i+1
workbook.save('TypeAnalysis.xls')