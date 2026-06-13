import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

# === Load data ===
df = pd.read_csv(r"../data/cleaned_genes.csv")
df = df.dropna(subset=["Gene", "Resistance_Type"])

# === Build graph ===
G = nx.Graph()
for _, row in df.iterrows():
    gene = str(row["Gene"]).strip()
    category = str(row["Resistance_Type"]).strip()
    G.add_node(gene, type="gene")
    G.add_node(category, type="category")
    G.add_edge(gene, category)

# === Define fixed positions for categories (corners) ===
categories = list({str(row["Resistance_Type"]).strip() for _, row in df.iterrows()})
corner_positions = {
    cat: pos for cat, pos in zip(categories, [
        (-1, 1),   # Top-left
        (1, 1),    # Top-right
        (-1, -1),  # Bottom-left
        (1, -1),   # Bottom-right
        (0, 1.5),  # Top-center (if needed)
        (1.5, 0),  # Right-center (if needed)
        (-1.5, 0), # Left-center (if needed)
        (0, -1.5), # Bottom-center (if needed)
    ])
}

# Kamada-Kawai layout with fixed positions
pos = nx.kamada_kawai_layout(G, pos=corner_positions, fixed=corner_positions.keys())

# === Node style ===
plt.figure(figsize=(22, 20))
nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.6)

# Separate node lists
category_nodes = [n for n in G if G.nodes[n]["type"] == "category"]
gene_nodes = [n for n in G if G.nodes[n]["type"] == "gene"]

# Draw categories
nx.draw_networkx_nodes(G, pos, nodelist=category_nodes, node_color="salmon", node_size=800, label="Stress Types")
nx.draw_networkx_labels(G, pos, labels={n: n for n in category_nodes}, font_size=12, font_weight="bold")

# Draw genes
nx.draw_networkx_nodes(G, pos, nodelist=gene_nodes, node_color="skyblue", node_size=300, label="Genes")
nx.draw_networkx_labels(G, pos, labels={n: n for n in gene_nodes}, font_size=6)

# === Title and legend ===
plt.title("Gene–Function Network (Stress Types in Corners)", fontsize=16)
plt.axis("off")

# Legend
legend_handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Genes', markersize=10, markerfacecolor='skyblue'),
    plt.Line2D([0], [0], marker='o', color='w', label='Stress Types', markersize=10, markerfacecolor='salmon')
]
plt.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# === Save ===
output_path = "../output/enhanced_gene_function_network_spread2.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()
