import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to your main CSV (adjust if using a different file)
CSV_PATH = "ufc_combined_1994_2024.csv"

# Directory where figures are stored
FIGURES_DIR = "figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

# 1. Load the CSV into a DataFrame
df = pd.read_csv(CSV_PATH)

# 2. Identify which column holds the fight date
#    We look for any column name containing "date" (case‐insensitive)
date_candidates = [col for col in df.columns if "date" in col.lower()]
if not date_candidates:
    raise ValueError("No column containing 'date' found in CSV.")
date_col = date_candidates[0]  # e.g., "date" or "Date"

# 3. Identify which column holds the weight class
#    We look for any column name containing "weight" (case‐insensitive)
weight_candidates = [col for col in df.columns if "weight" in col.lower()]
if not weight_candidates:
    raise ValueError("No column containing 'weight' found in CSV.")
weight_col = weight_candidates[0]  # e.g., "weight_class" or "Weight Class"

# 4. Parse the fight date column into datetime
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df = df.dropna(subset=[date_col])  # drop rows where date couldn’t be parsed

# 5. Infer gender from weight_class
#    Any weight_class value that starts with "Women" (case‐insensitive) → "Female"
def infer_gender(wc):
    if isinstance(wc, str) and wc.lower().startswith("women"):
        return "Female"
    else:
        return "Male"

df["gender"] = df[weight_col].apply(infer_gender)

# 6. Extract year from the fight date
df["year"] = df[date_col].dt.year

# 7. Group by year and gender, count number of fights per group
counts = df.groupby(["year", "gender"]).size().unstack(fill_value=0)

# 8. Ensure both "Male" and "Female" columns exist
for g in ["Male", "Female"]:
    if g not in counts.columns:
        counts[g] = 0
counts = counts.sort_index()

# 9. Plot the annual fight counts
plt.figure(figsize=(10, 6))
plt.plot(counts.index, counts["Male"], label="Male", linewidth=2)
plt.plot(counts.index, counts["Female"], label="Female", linewidth=2)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of UFC Fights", fontsize=12)
plt.title("Annual UFC Fight Count by Gender (1994–2024)", fontsize=14)
plt.legend(title="Gender")
plt.grid(alpha=0.3)

# 10. Save the figure
output_path = os.path.join(FIGURES_DIR, "annual_fight_counts_by_gender.png")
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Saved annual fight count plot to: {output_path}")
