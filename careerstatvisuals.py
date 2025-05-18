import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create 'figures' directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

# Load dataset
df = pd.read_csv('fighters_with_career_stats.csv')

# Descriptive stats by gender
summary = df.groupby('gender')[['age_at_start', 'num_fights', 'career_span_years']].describe()
print(summary)

# Plot 1: Career span by gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='career_span_years', data=df)
plt.title('Career Span by Gender')
plt.tight_layout()
plt.savefig('figures/career_span_by_gender.png', dpi=300)
plt.show()

# Plot 2: Age at career start by gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='age_at_start', data=df)
plt.title('Age at Career Start by Gender')
plt.tight_layout()
plt.savefig('figures/age_at_start_by_gender.png', dpi=300)
plt.show()

# Plot 3: Distribution of fight counts by gender
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='num_fights', hue='gender', bins=20, kde=True)
plt.title('Distribution of Fight Counts by Gender')
plt.tight_layout()
plt.savefig('figures/fight_count_distribution_by_gender.png', dpi=300)
plt.show()
