import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "ufc_combined_1994_2024.csv"

FIGURES_DIR = "figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)

date_candidates = [col for col in df.columns if "date" in col.lower()]
if not date_candidates:
    raise ValueError("No column containing 'date' found in CSV.")
date_col = date_candidates[0]  # e.g., "date" or "Date"

weight_candidates = [col for col in df.columns if "weight" in col.lower()]
if not weight_candidates:
    raise ValueError("No column containing 'weight' found in CSV.")
weight_col = weight_candidates[0]  # e.g., "weight_class" or "Weight Class"

df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df = df.dropna(subset=[date_col])  # drop rows where date couldn’t be parsed

def infer_gender(wc):
    if isinstance(wc, str) and wc.lower().startswith("women"):
        return "Female"
    else:
        return "Male"

df["gender"] = df[weight_col].apply(infer_gender)

 
df["year"] = df[date_col].dt.year
 
counts = df.groupby(["year", "gender"]).size().unstack(fill_value=0)
 
for g in ["Male", "Female"]:
    if g not in counts.columns:
        counts[g] = 0
counts = counts.sort_index()
 
plt.figure(figsize=(10, 6))
plt.plot(counts.index, counts["Male"], label="Male", linewidth=2)
plt.plot(counts.index, counts["Female"], label="Female", linewidth=2)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of UFC Fights", fontsize=12)
plt.title("Annual UFC Fight Count by Gender (1994–2024)", fontsize=14)
plt.legend(title="Gender")
plt.grid(alpha=0.3)
 
output_path = os.path.join(FIGURES_DIR, "annual_fight_counts_by_gender.png")
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Saved annual fight count plot to: {output_path}")
