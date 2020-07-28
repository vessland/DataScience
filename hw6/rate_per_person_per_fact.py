import os

import pandas as pd
import numpy as np
import openpyxl

data = pd.read_csv(r"rate.csv")

tmp = data.iloc[:, [0,3,4,5,6,7,8,9,10]]
with pd.ExcelWriter('./rate_per_person_per_fact.xls') as writer:
    tmp.groupby(["user_id"]).mean().to_excel(writer)