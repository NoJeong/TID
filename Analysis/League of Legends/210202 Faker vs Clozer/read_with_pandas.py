import pandas as pd
import openpyxl

two_mid = pd.read_excel('../raw DATA/210131MID.xlsx', usecols=[0, 2, 3, 6, 10, 11, 17, 19], skiprows=[1,2,3,5,6,7,8,9,11])

print(two_mid)