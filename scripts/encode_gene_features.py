import pandas as pd

# Load gene dataset
gene_path = "../data/categorized_stress_response_genes.csv"
genes_df = pd.read_csv(gene_path)

# Drop rows without Resistance_Type
genes_df = genes_df.dropna(subset=['Resistance_Type'])

# Report dropped rows
print(f"📉 Rows after dropping missing Resistance_Type: {len(genes_df)}")

# One-hot encode resistance types
encoded = pd.get_dummies(genes_df['Resistance_Type'])

# Combine with Extremophile
encoded['Extremophile'] = genes_df['Extremophile']

# Group by Extremophile
aggregated = encoded.groupby('Extremophile').sum().reset_index()

# Save to the new path
output_path = "../data/aggregated_gene_features.csv"
aggregated.to_csv(output_path, index=False)

print("\n🧬 Aggregated gene features saved to:", output_path)
print("\n🧪 Final preview:")
print(aggregated.head())
