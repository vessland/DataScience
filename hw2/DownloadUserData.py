import json
import urllib.request, urllib.parse
import os

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
for key, values in data.items():
    if (os.path.exists(str(values['user_id']))):
        print("已存在用户文件夹：" + str(values['user_id']))
        cases = values['cases']
        for case in cases:
            filenamePath = urllib.parse.unquote(os.path.basename(case["case_zip"]))
            if (filenamePath[0:3] == "N*N"):
                filenamePath = filenamePath[3:]
            if (os.path.exists(str(values['user_id']) + '//' + filenamePath)):
                print("已存在题目文件夹：" + filenamePath)
                uploads = case["upload_records"]
                for upload in uploads:
                    if (os.path.exists(str(values['user_id']) + '//' + filenamePath + "//" + str(
                            upload["upload_id"]) + ".zip")):
                        print("已存在上传记录：" + str(upload["upload_id"]) + ".zip")
                    else:
                        if (upload["upload_id"] != 308630):
                            filename = str(upload["upload_id"])
                            url = upload["code_url"]
                            print("正在下载：" + filename)
                            urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filenamePath + "//" + str(
                            upload["upload_id"]) + ".zip")
            else:
                os.makedirs(str(values['user_id']) + '//' + filenamePath)
                uploads = case["upload_records"]
                for upload in uploads:
                    filename = str(upload["upload_id"])
                    url = upload["code_url"]
                    print("正在下载：" + filename)
                    urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filenamePath + "//" + str(
                        upload["upload_id"]) + ".zip")
    else:
        cases = values['cases']
        os.mkdir(str(values['user_id']))
        for case in cases:
            filenamePath = urllib.parse.unquote(os.path.basename(case["case_zip"]))
            if (filenamePath[0:3] == "N*N"):
                filenamePath = filenamePath[3:]
            if (not os.path.exists(str(values['user_id']) + '//' + filenamePath)):
                os.makedirs(str(values['user_id']) + '//' + filenamePath)
            uploads = case["upload_records"]
            for upload in uploads:
                filename = str(upload["upload_id"])
                url = upload["code_url"]
                print("正在下载：" + filename)
                urllib.request.urlretrieve(url, str(values['user_id']) + '//' + filenamePath + "//" + str(
                    upload["upload_id"]) + ".zip")
