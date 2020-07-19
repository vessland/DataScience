import os
os.chdir(r"C:\Users\DELL\Desktop")

import pandas as pd
import numpy as np

data = pd.read_excel(r"./CodeLinesAnalysis.xls")

tmp = data.iloc[:, [1, 3]]
with pd.ExcelWriter('./codeLinesAvr.xlsx') as writer:
    tmp.groupby(["case_id"]).mean().to_excel(writer)