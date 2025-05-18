from scipy.stats import f_oneway
import pandas as pd

# Load dataset
df = pd.read_csv('fighters_with_career_stats.csv')

# Filter to female fighters only
female_df = df[df['gender'].str.lower() == 'female']

# Get top 5 countries by number of female fighters
top_countries = female_df['country'].value_counts().head(5).index.tolist()

# Prepare grouped data for each metric
span_groups = [female_df[female_df['country'] == country]['career_span_years'].dropna() for country in top_countries]
age_groups = [female_df[female_df['country'] == country]['age_at_start'].dropna() for country in top_countries]
fight_groups = [female_df[female_df['country'] == country]['num_fights'].dropna() for country in top_countries]

# ANOVA Tests
f_span, p_span = f_oneway(*span_groups)
f_age, p_age = f_oneway(*age_groups)
f_fights, p_fights = f_oneway(*fight_groups)

# Print Results
print("ANOVA Results (Top 5 Countries by Female Fighter Count):")
print(f"Career Span Years: F = {f_span:.2f}, p = {p_span:.4f}")
print(f"Age at Career Start: F = {f_age:.2f}, p = {p_age:.4f}")
print(f"Number of Fights: F = {f_fights:.2f}, p = {p_fights:.4f}")
