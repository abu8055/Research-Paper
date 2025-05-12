import pandas as pd


df1 = pd.read_csv('fighters_with_gender.csv')
df2 = pd.read_csv('ALL UFC FIGHTERS 2_23_2016 SHERDOG.COM.csv')

df1_clean = df1[['name', 'gender']].drop_duplicates()
df2_merged = df2.merge(df1_clean, on='name', how='left')

df2_merged.to_csv('file2_with_gender.csv',index=False)