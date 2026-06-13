import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load data
input_csv = "../data/aggregated_gene_features.csv"
output_dir = "../output"

df = pd.read_csv(input_csv)

# Set 'Extremophile' as index and normalize feature values for better radar plot scaling
df.set_index('Extremophile', inplace=True)
features = df.columns

# Normalize the features (min-max normalization)
df_normalized = (df - df.min()) / (df.max() - df.min())

# Create radar plots
for extremophile in df_normalized.index:
    values = df_normalized.loc[extremophile].tolist()
    values += values[:1]  # Repeat the first value to close the circular graph

    angles = np.linspace(0, 2 * np.pi, len(features), endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=2, linestyle='solid', label=extremophile)
    ax.fill(angles, values, alpha=0.25)

    ax.set_title(f"{extremophile} - Stress Adaptation Profile", size=14)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(features, fontsize=9)

    ax.set_yticklabels([])  # Hide radial labels
    ax.grid(True)

    # Save figure
    output_path = os.path.join(output_dir, f"{extremophile}_radar_plot.png")
    plt.savefig(output_path)
    plt.close()

print("✅ Radar plots saved successfully.")
