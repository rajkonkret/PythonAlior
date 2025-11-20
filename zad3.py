import pandas as pd

df = pd.read_csv('AAPL_stock_price_example.csv')
print(df)

print(df.describe())

#              Close
# count  229.000000
# mean   201.477598
# std     28.246961
# min    142.190002
# 25%    182.539993
# 50%    200.720001
# 75%    213.279999
# max    267.100006
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 229 entries, 0 to 228
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Date    229 non-null    object
#  1   Close   229 non-null    float64
# dtypes: float64(1), object(1)
# memory usage: 3.7+ KB

df.to_excel("dane_akcje.xlsx")
# pip install openpyxl