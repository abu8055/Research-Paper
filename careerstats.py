import pandas as pd

# Load the datasets
fighters_df = pd.read_csv('ufc_fighters_cleaned.csv')  # Adjust filename as needed
fights_df = pd.read_csv('ufc_combined_1994_2024.csv')

# Parse dates
fighters_df['birth_date'] = pd.to_datetime(fighters_df['birth_date'], errors='coerce')
fights_df['Date'] = pd.to_datetime(fights_df['Date'], errors='coerce')

# Reshape fights to long format: one row per fighter per fight
red_fights = fights_df[['Date', 'RedFighter']].rename(columns={'RedFighter': 'name'})
blue_fights = fights_df[['Date', 'BlueFighter']].rename(columns={'BlueFighter': 'name'})
all_fights = pd.concat([red_fights, blue_fights], ignore_index=True)

# Merge birth dates
fight_data = all_fights.merge(fighters_df[['name', 'birth_date']], on='name', how='left')

# Calculate age at fight
fight_data['age_at_fight'] = (fight_data['Date'] - fight_data['birth_date']).dt.days / 365.25

# Group by fighter to calculate career stats
career_stats = fight_data.groupby('name').agg(
    career_start=('Date', 'min'),
    career_end=('Date', 'max'),
    num_fights=('Date', 'count'),
    age_at_start=('age_at_fight', 'min')
).reset_index()

career_stats['career_span_years'] = (career_stats['career_end'] - career_stats['career_start']).dt.days / 365.25

# Merge with fighters dataframe
fighters_augmented = fighters_df.merge(
    career_stats[['name', 'age_at_start', 'num_fights', 'career_span_years']],
    on='name',
    how='left'
)

# Save to new file
fighters_augmented.to_csv('fighters_with_career_stats.csv', index=False)
