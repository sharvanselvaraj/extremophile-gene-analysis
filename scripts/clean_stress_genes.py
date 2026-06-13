import pandas as pd
import os

# Load the original dataset
input_path = "../data/categorized_stress_response_genes.csv"
df = pd.read_csv(input_path)

# Drop rows where 'Gene' is missing
df_cleaned = df.dropna(subset=['Gene'])

# Reset index
df_cleaned.reset_index(drop=True, inplace=True)

# Define the new output path
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "cleaned_genes.csv")

# Save cleaned data
df_cleaned.to_csv(output_path, index=False)

print(f"Cleaned gene data saved to: {output_path}")
