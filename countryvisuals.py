import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv('fighters_with_career_stats.csv')

# Filter for female fighters
females = df[df['gender'].str.lower() == 'female']
females = females.dropna(subset=['country'])

# Group by country and calculate metrics
country_stats = females.groupby('country').agg({
    'name': 'count',
    'age_at_start': 'mean',
    'num_fights': 'mean',
    'career_span_years': 'mean'
}).rename(columns={'name': 'num_female_fighters'}).round(2)

# Filter to countries with at least 3 female fighters
country_stats_filtered = country_stats[country_stats['num_female_fighters'] >= 3]

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Plot 1: Top countries by number of female fighters
top_by_fighter_count = country_stats_filtered.sort_values(by='num_female_fighters', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_by_fighter_count['num_female_fighters'], y=top_by_fighter_count.index, palette='Blues_d')
plt.title('Top Countries by Number of Female UFC Fighters')
plt.xlabel('Number of Female Fighters')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('figures/num_female_fighters_by_country.png', dpi=300)
plt.show()

# Plot 2: Top countries by average career span
top_by_span = country_stats_filtered.sort_values(by='career_span_years', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_by_span['career_span_years'], y=top_by_span.index, palette='Purples_d')
plt.title('Top Countries by Avg Career Span (Female UFC Fighters)')
plt.xlabel('Average Career Span (Years)')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('figures/career_span_by_country.png', dpi=300)
plt.show()

# Plot 3: Age at career start by country
top_by_age = country_stats_filtered.sort_values(by='age_at_start', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_by_age['age_at_start'], y=top_by_age.index, palette='Greens_d')
plt.title('Top Countries by Avg Age at Career Start (Female Fighters)')
plt.xlabel('Average Age at Start')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('figures/age_at_start_by_country.png', dpi=300)
plt.show()

# Plot 4: Number of fights by country
top_by_fights = country_stats_filtered.sort_values(by='num_fights', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_by_fights['num_fights'], y=top_by_fights.index, palette='Oranges_d')
plt.title('Top Countries by Avg Number of Fights (Female Fighters)')
plt.xlabel('Average Number of Fights')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('figures/num_fights_by_country.png', dpi=300)
plt.show()
