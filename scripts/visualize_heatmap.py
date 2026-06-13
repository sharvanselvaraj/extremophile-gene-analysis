import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the data
file_path = "../data/aggregated_gene_features.csv"
df = pd.read_csv(file_path)

# Set the output path
output_dir = "../output"
output_file = os.path.join(output_dir, "extremophile_resistance_heatmap.png")

# Set the extremophile as the index
df.set_index('Extremophile', inplace=True)

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='YlGnBu', linewidths=0.5, fmt=".1f", cbar_kws={'label': 'Gene Count'})
plt.title("Stress Resistance Profile of Extremophiles")
plt.ylabel("Extremophile")
plt.xlabel("Stress Resistance Type")
plt.tight_layout()

# Save the heatmap
plt.savefig(output_file)
plt.show()
