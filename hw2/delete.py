import os
import zipfile
infiles=os.listdir()
for file in infiles:
    if file.isdigit():
        onfiles=os.listdir(file+"//")
        for f in onfiles:
            zipfiles=os.listdir(file+"//"+f+"//")
            for ff in zipfiles:
                if ff[-4:]==".zip":
                   os.remove(file + "//"+f+"//" + ff)
                   print("正在删除：" + ff)