import pandas as pd
import networkx as nx

# Load cleaned dataset
df = pd.read_csv(r"../data/cleaned_genes.csv")
df = df.dropna(subset=["Gene", "Resistance_Type"])

# Build network
G = nx.Graph()
for _, row in df.iterrows():
    gene = str(row["Gene"]).strip()
    category = str(row["Resistance_Type"]).strip()
    G.add_node(gene, type="gene")
    G.add_node(category, type="category")
    G.add_edge(gene, category)

# Calculate centrality metrics
degree_centrality = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
node_types = nx.get_node_attributes(G, "type")

# Build metrics DataFrame
metrics = []
for node in G.nodes():
    metrics.append({
        "Node": node,
        "Type": node_types.get(node, "unknown"),
        "Degree": G.degree[node],
        "Degree_Centrality": degree_centrality[node],
        "Betweenness_Centrality": betweenness[node]
    })

metrics_df = pd.DataFrame(metrics)

# Save to updated path
output_path = "../output/network_metrics.csv"
metrics_df.to_csv(output_path, index=False)

# Print top insights
top_genes = metrics_df[metrics_df["Type"] == "gene"].sort_values(by="Degree", ascending=False).head(10)
top_stress = metrics_df[metrics_df["Type"] == "category"].sort_values(by="Degree", ascending=False).head(5)

print("Top 10 Hub Genes:")
print(top_genes[["Node", "Degree"]])

print("\nTop 5 Stress Types by Gene Count:")
print(top_stress[["Node", "Degree"]])
