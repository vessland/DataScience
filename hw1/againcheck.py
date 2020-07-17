import json
import urllib.request,urllib.parse
import os
f=open('test_data.json',encoding='utf-8')
res=f.read()
data=json.loads(res)
for key,values in data.items():
    if (os.path.exists(str(values['user_id']))):
        print("已存在文件夹：" + str(values['user_id']))
        cases = values['cases']
        for case in cases:
            filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
            if (filename[0:3] == "N*N"):
                filename = filename[3:]
            if (os.path.exists(str(values['user_id']) + '//' + filename[:-4])):
                print("已存在文件：" + filename)
            else:
                url = urllib.parse.quote(case["case_zip"], safe='/:?=')
                print("正在下载：" + filename)
                urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filename)
    else:
        cases = values['cases']
        os.mkdir(str(values['user_id']))
        for case in cases:
            filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
            url = urllib.parse.quote(case["case_zip"], safe='/:?=')
            print("正在下载：" + filename)
            if (filename[0:3] == "N*N"):
                urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filename[3:])
            else:
                urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filename)