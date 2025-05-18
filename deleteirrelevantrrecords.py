import pandas as pd

df= pd.read_csv('file2_with_gender.csv')
df_cleaned=df.dropna(subset=['birth_date','country','gender'])
df_cleaned.reset_index(drop=True, inplace=True)
df_cleaned.to_csv('ufc_fighters_cleaned.csv', index=False)
