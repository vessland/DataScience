import os
os.chdir(r"C:\Users\DELL\Desktop")

import pandas as pd
import numpy as np

data = pd.read_excel(r"./TimeAnalysis.xls")

tmp = data.iloc[:, [1, 2]]
with pd.ExcelWriter('./timeAvr.xlsx') as writer:
    tmp.groupby(["case_id"]).mean().to_excel(writer)