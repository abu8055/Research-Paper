import pandas as pd
from datetime import datetime

df = pd.read_csv('ufc_fighters_cleaned.csv')
df_cleaned = df.dropna(subset=['birth_date', 'country', 'gender']).copy()
df_cleaned['birth_date'] = pd.to_datetime(df_cleaned['birth_date'], errors='coerce')
today = pd.to_datetime('today')
df_cleaned['age'] = df_cleaned['birth_date'].apply(
    lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day))
)
df_cleaned.to_csv('ufc_fighters_cleaned.csv', index=False)

