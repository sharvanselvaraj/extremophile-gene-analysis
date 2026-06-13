import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import os

# ==== Paths ====
input_path = "../data/aggregated_gene_features.csv"
output_dir = "../output"
os.makedirs(output_dir, exist_ok=True)

# ==== Load Data ====
df = pd.read_csv(input_path)
df.set_index("Extremophile", inplace=True)

# ==== Normalize Data ====
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# ==== Perform Clustering ====
cluster = AgglomerativeClustering(n_clusters=3)  # Adjust the number of clusters as needed
df['Cluster'] = cluster.fit_predict(scaled_data)

# ==== Save clustered data ====
clustered_output = os.path.join(output_dir, "extremophile_clusters.csv")
df.to_csv(clustered_output)

# ==== Clustered Heatmap ====
plt.figure(figsize=(12, 8))
sns.clustermap(df.drop("Cluster", axis=1), method='ward', cmap='coolwarm', standard_scale=1, figsize=(12, 10))
plt.savefig(os.path.join(output_dir, "extremophile_clusters_heatmap.png"))
plt.close()

print("✅ Clustering complete.")
print(f"📁 Clustered CSV saved to: {clustered_output}")
print(f"🖼️ Heatmap saved to: {os.path.join(output_dir, 'extremophile_clusters_heatmap.png')}")
