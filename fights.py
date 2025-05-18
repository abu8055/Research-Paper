import pandas as pd

df_master = pd.read_csv("ufc-master.csv")
df_complete = pd.read_csv("complete_ufc_data.csv")

df_master['Date'] = pd.to_datetime(df_master['Date'])
df_complete['event_date'] = pd.to_datetime(df_complete['event_date'])

df_complete_pre2010 = df_complete[df_complete['event_date'].dt.year < 2010]

df_complete_pre2010 = df_complete_pre2010.rename(columns={
    'event_date': 'Date',
    'fighter1': 'RedFighter',
    'fighter2': 'BlueFighter',
    'weight_class': 'WeightClass',
    'outcome': 'Winner',
    'method': 'Finish'
})

for col in df_master.columns:
    if col not in df_complete_pre2010.columns:
        df_complete_pre2010[col] = None

df_complete_pre2010 = df_complete_pre2010[df_master.columns]

df_combined = pd.concat([df_master, df_complete_pre2010], ignore_index=True)

df_combined.to_csv("ufc_combined_1994_2024.csv", index=False)

