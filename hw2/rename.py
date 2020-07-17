import os

infiles=os.listdir()
for file in infiles:
    if file.isdigit():
        onfiles=os.listdir(file+"//")
        for f in onfiles:
            if f[-4:]==".zip":
                os.rename(file+"//"+f,file+"//"+f[:-4])