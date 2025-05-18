import pandas as pd

# Load the updated fighters file
df = pd.read_csv('fighters_with_career_stats.csv')

df['age_at_start'] = df['age_at_start'].round(2)
df['career_span_years'] = df['career_span_years'].round(2)

df.to_csv('fighters_with_career_stats.csv', index=False)
