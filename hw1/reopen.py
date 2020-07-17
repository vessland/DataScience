import os
import zipfile
infiles=os.listdir()
for file in infiles:
    if file.isdigit():
        onfiles=os.listdir(file+"//")
        for f in onfiles:
            if f[-4:]==".zip":
                zip_file = zipfile.ZipFile(file + "//" + f)
                os.mkdir(file + "//" + f[:-4])
                zip_file.extractall(file + "//" + f[:-4])
                print("正在解压：" + f)