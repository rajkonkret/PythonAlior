import pandas as pd

df = pd.read_csv('evolution_of_data_analysis.csv', delimiter="|")
print(df)
print(df.describe())

#               Year
# count    42.000000
# mean   1993.833333
# std      18.876901
# min    1945.000000
# 25%    1987.500000
# 50%    1999.000000
# 75%    2006.750000
# max    2018.000000

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 42 entries, 0 to 41
# Data columns (total 7 columns):
#  #   Column                            Non-Null Count  Dtype
# ---  ------                            --------------  -----
#  0   Year                              42 non-null     int64
#  1   Decade                            42 non-null     object
#  2   Milestone Title                   42 non-null     object
#  3   Milestone Event                   42 non-null     object
#  4   Why Important                     42 non-null     object
#  5   Reference                         39 non-null     object
#  6   People Process or Technology Tag  42 non-null     object
# dtypes: int64(1), object(6)
# memory usage: 2.4+ KB