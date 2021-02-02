import pandas as pd
import openpyxl

df_use_skip = pd.read_excel('../raw DATA/210131MID.csv', usecols=[0, 1, 3])

print(df_use_skip)