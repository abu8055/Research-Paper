from scipy.stats import ttest_ind
import pandas as pd
df = pd.read_csv('fighters_with_career_stats.csv')
males = df[df['gender'].str.lower() == 'male']
females = df[df['gender'].str.lower() == 'female']

# Career span
t1, p1 = ttest_ind(males['career_span_years'].dropna(), females['career_span_years'].dropna())

# Age at start
t2, p2 = ttest_ind(males['age_at_start'].dropna(), females['age_at_start'].dropna())

# Number of fights
t3, p3 = ttest_ind(males['num_fights'].dropna(), females['num_fights'].dropna())

print(f"Career span: t={t1:.2f}, p={p1:.4f}")
print(f"Age at start: t={t2:.2f}, p={p2:.4f}")
print(f"Number of fights: t={t3:.2f}, p={p3:.4f}")
