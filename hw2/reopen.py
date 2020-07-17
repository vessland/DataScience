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
                    if( not os.path.exists(file+"//"+f+"//"+ ff[:-4])):
                        zip_file = zipfile.ZipFile(file+"//"+f+"//"+ff)
                        os.mkdir(file + "//" + f + "//" + ff[:-4])
                        zip_file.extractall(file + "//" + f + "//" + ff[:-4])
                        print("正在解压：" + ff)
