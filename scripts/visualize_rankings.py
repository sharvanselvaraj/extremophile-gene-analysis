import pandas as pd
import matplotlib.pyplot as plt
import os

# === INPUT FILE ===
input_csv = "../data/aggregated_gene_features.csv"

# === OUTPUT FOLDER ===
output_dir = "../output"
os.makedirs(output_dir, exist_ok=True)

# === Load Data ===
df = pd.read_csv(input_csv)

# === Drop non-numeric column ===
extremophiles = df['Extremophile']
features = df.drop(columns=['Extremophile'])

# === Calculate Stress Resistance Score ===
df['Stress_Resistance_Score'] = features.sum(axis=1)

# === Save updated CSV ===
output_csv = os.path.join(output_dir, "extremophile_resistance_scores.csv")
df[['Extremophile', 'Stress_Resistance_Score']].to_csv(output_csv, index=False)

# === Plot Bar Chart ===
plt.figure(figsize=(10, 6))
plt.bar(df['Extremophile'], df['Stress_Resistance_Score'], color='steelblue')
plt.xlabel("Extremophile")
plt.ylabel("Stress Resistance Score")
plt.title("Stress Resistance Score per Extremophile")
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
output_plot = os.path.join(output_dir, "resistance_score_barplot.png")
plt.savefig(output_plot, dpi=300)
plt.close()

print("✅ Stress resistance scores saved to:")
print(output_csv)
print("📊 Barplot saved to:")
print(output_plot)
