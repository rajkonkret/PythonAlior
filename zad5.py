import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv', index_col="Title")
print(df)
print(df.describe())
print(70 * "-")
print(df.info())
print(df.duplicated().any())  # False
print("Ilość duplikatów:", df.duplicated().sum())  # Ilość duplikatów: 0
print(df.drop_duplicates())
# po doodaniu wierszza
# True
# Ilość duplikatów: 1
print(df.drop_duplicates(subset=["Director"]))  # gdy dane w kolumnie sie powtarzają

df_new = df.rename(columns={"Runtime (Minutes)": "Runtime"})  # nowa tablica ze zmianami
print(df_new)
df_new.info()  # 6   Runtime
df.rename(columns={"Runtime (Minutes)": "Runtime"}, inplace=True)  # inplce - zmiana oryginału
print(df.info())  # 6   Runtime

df.isnull().sum().to_json("dane2345.json") # policzone ile jest null

movies_df_not_null = df.dropna() # usun nnulle (NaN), zwraca nowa kolekcję
movies_df_not_null.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 839 entries, Guardians of the Galaxy to Nine Lives
# Data columns (total 11 columns):
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   Rank                839 non-null    int64
#  1   Genre               839 non-null    object
#  2   Description         839 non-null    object
#  3   Director            839 non-null    object
#  4   Actors              839 non-null    object
#  5   Year                839 non-null    int64
#  6   Runtime             839 non-null    int64
#  7   Rating              839 non-null    float64
#  8   Votes               839 non-null    int64
#  9   Revenue (Millions)  839 non-null    float64
#  10  Metascore           839 non-null    float64
# dtypes: float64(3), int64(4), object(4)
# memory usage: 78.7+ KB
rev = df['Revenue (Millions)']
print(rev.head())
# dtypes: float64(3), int64(4), object(4)
# memory usage: 78.7+ KB
# Title
# Guardians of the Galaxy    333.13
# Prometheus                 126.46
# Split                      138.12
# Split                      138.12
# Sing                       270.32
# Name: Revenue (Millions), dtype: float64
rev.info()
# <class 'pandas.core.series.Series'>
# Index: 1001 entries, Guardians of the Galaxy to Nine Lives
# Series name: Revenue (Millions)
# Non-Null Count  Dtype
# --------------  -----
# 873 non-null    float64
# dtypes: float64(1)
# memory usage: 47.9+ KB