import json
import os
import xlwt
import urllib.parse
import _locale
import radon

_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

workbook=xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0,"user_id")
worksheet.write(0,1,"case_id")
worksheet.write(0,2,"answer_rate")
f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
i=1
for key, values in data.items():
    cases = values['cases']
    for case in cases:
        worksheet.write(i,0,values['user_id'])
        worksheet.write(i,1,case['case_id'])
        uploads=case["upload_records"]
        if(len(uploads)>0):
            filenamePath = urllib.parse.unquote(os.path.basename(case["case_zip"]))
            if (filenamePath[0:3] == "N*N"):
                filenamePath = filenamePath[3:]
            filenamePath = filenamePath[:-4]
            if (os.path.exists(str(values['user_id']) + "//" + filenamePath+"//"+str(uploads[-1]['upload_id']))):
                os.system(r"cd C:\Users\16484\AppData\Local\Programs\Python\Python37\Lib\site-packages")
                comand = r"radon mi "+str(values['user_id']) + "//" + filenamePath + "//"+str(uploads[-1]['upload_id'])+"//main.py" + " -s"
                d = os.popen(comand)
                f = d.read()
                print(f)
                if len(f) > 12:
                    if f[-12] == '(':
                        print(float(f[-11:-6]))
                        worksheet.write(i,2,float(f[-11:-6]))
                    elif f[-13] == '(':
                        print(100.00)
                        worksheet.write(i,2,100.00)
                    else:
                        print(0.00)
                        worksheet.write(i,2,0.0)
                else:
                    print(0.00)
                    worksheet.write(i, 2, 0.0)
            else:
                worksheet.write(i, 2, 0.0)
        i=i+1
        print(i)
workbook.save('rateAnalysis.xls')





