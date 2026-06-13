import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned gene data
input_path = "../data/cleaned_genes.csv"
df = pd.read_csv(input_path)

# Drop rows with missing Resistance_Type or Product
df = df.dropna(subset=["Resistance_Type", "Product"])

# Group by Resistance Type and Product, then count occurrences
product_counts = df.groupby(["Resistance_Type", "Product"]).size().reset_index(name="Count")

# Sort each group by count and take top 5 most common products per resistance type
top_products = product_counts.groupby("Resistance_Type").apply(
    lambda x: x.sort_values("Count", ascending=False).head(5)
).reset_index(drop=True)

# Set up the plot
plt.figure(figsize=(14, 8))
sns.barplot(
    data=top_products,
    x="Count", y="Product",
    hue="Resistance_Type"
)
plt.title("Top 5 Gene Products by Stress Resistance Type", fontsize=16)
plt.xlabel("Gene Count")
plt.ylabel("Gene Product")
plt.legend(title="Resistance Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = "../output/top_gene_products_by_stress_type.png"
plt.savefig(output_path, dpi=300)
plt.show()
