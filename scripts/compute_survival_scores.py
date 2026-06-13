import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

# Set paths
input_path = "../data/aggregated_gene_features.csv"
output_path = "../data/extremophile_survival_scores.csv"

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Load data
df = pd.read_csv(input_path)
print(f"✅ Loaded gene matrix: {df.shape[0]} extremophiles, {df.shape[1] - 1} stress features")

# Separate features and apply MinMax scaling
extremophiles = df['Extremophile']
features = df.drop(columns='Extremophile')

# Normalize all feature columns to [0,1]
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Calculate continuous survival score as the sum of normalized stress resistance features
df['Survival_Score'] = normalized_features.sum(axis=1)

# Round for neatness
df['Survival_Score'] = df['Survival_Score'].round(4)

# Select only relevant columns for output
output_df = df[['Extremophile', 'Survival_Score']]

# Preview
print("\n🧪 Preview of survival scores:")
print(output_df.head())

# Save to CSV
output_df.to_csv(output_path, index=False)
print(f"\n✅ Survival scores saved to: {output_path}")
