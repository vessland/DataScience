import json
import urllib.request, urllib.parse
import os

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
for key, values in data.items():
    cases = values['cases']
    for case in cases:
        filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        if (filename[0:3] == "N*N"):
            filename = filename[3:]
        filename=filename[:-4]
        if (os.path.exists(str(values['user_id']) + '//' + filename)):
            os.rename(str(values['user_id']) + '//' + filename,str(values['user_id']) + '//' + str(case['case_id']))