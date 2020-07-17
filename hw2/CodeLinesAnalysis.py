import json
import os
import xlwt
import urllib.parse

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"answer_lines")
worksheet.write(0,3,"final_lines")
worksheet.write(0,4,"each_code_lines")
f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
i=1
for key, values in data.items():
    cases = values['cases']
    for case in cases:
        finallines=0
        answerlines=0
        uploads=case["upload_records"]
        worksheet.write(i,0,values['user_id'])
        worksheet.write(i,1,case['case_id'])
        if(len(uploads)>0):
            for j in range(0, len(uploads)):
                filenamePath = urllib.parse.unquote(os.path.basename(case["case_zip"]))
                if (filenamePath[0:3] == "N*N"):
                    filenamePath = filenamePath[3:]
                filenamePath=filenamePath[:-4]
                if(os.path.exists(str(values['user_id'])+"//"+filenamePath+"//"+str(uploads[j]['upload_id']))):
                    print("存在"+str(values['user_id'])+"//"+filenamePath+"//"+str(uploads[j]['upload_id'])+"//main.py")
                    lines = len(open(str(values['user_id'])+"//"+filenamePath+"//"+str(uploads[j]['upload_id'])+"//main.py", 'rU',encoding='UTF-8').readlines())
                    worksheet.write(i,4+j,lines)
                    finallines=lines
                    answerlines = len(open(str(values['user_id'])+"//"+filenamePath+"//"+str(uploads[j]['upload_id'])+"//.mooctest//answer.py", 'rU',encoding='UTF-8').readlines())
        worksheet.write(i,3,finallines)
        worksheet.write(i,2,answerlines)
        i=i+1
workbook.save('CodeLinesAnalysis.xls')