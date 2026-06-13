import pandas as pd

# File paths
input_file = "../data/combined_prokka.csv"
output_all_file = "../data/filtered_stress_response_genes.csv"
output_categorized_file = "../data/categorized_stress_response_genes.csv"

# Expanded stress-response keywords
stress_keywords = {
    "Radiation resistance": [
        "recA", "recF", "uvrA", "uvrB", "uvrC", "radA", "radB", "pprA", "ddrA", "ddrB", "ddrC", "ddrD",
        "oxidoreductase", "superoxide dismutase", "thioredoxin", "peroxidase", "antioxidant",
        "DNA repair", "DNA polymerase"
    ],
    "Salt tolerance": [
        "sodium/proton antiporter", "na+/h+ antiporter", "osmoregulation",
        "ion transporter", "osmoprotectant", "halotolerance", "salt adaptation",
        "compatible solute", "glycine betaine", "proline transporter", "osmotic"
    ],
    "Cold resistance": [
        "cold shock", "antifreeze", "cryoprotection", "cold-induced", "low-temperature",
        "RNA chaperone", "psychrophilic", "cspa", "cspb"
    ],
    "Heat resistance": [
        "heat shock", "chaperone", "thermophilic", "heat-induced", "thermostable",
        "HSP", "proteostasis", "protein folding", "groEL", "groES", "dnaK", "dnaJ"
    ],
    "Acidic environment adaptation": [
        "acid phosphatase", "proton pump", "acid resistance", "low pH", "acid tolerance",
        "acidic adaptation", "pH homeostasis", "buffer system", "glutamate decarboxylase"
    ],
    "Oxidative stress": [
        "superoxide dismutase", "catalase", "peroxidase", "oxidoreductase",
        "glutathione", "thioredoxin", "redox"
    ],
    "General stress response": [
        "universal stress protein", "USP", "stress response", "sensor kinase",
        "two-component system", "signal transduction"
    ]
}

# Load input data
data = pd.read_csv(input_file)

# Filter genes based on stress-related keywords
filtered_results = []
for _, row in data.iterrows():
    combined_text = f"{str(row.get('gene', '')).lower()} {str(row.get('product', '')).lower()}"
    extremophile = row.get("extremophile", "Unknown")
    matched = False

    for stress_type, keywords in stress_keywords.items():
        if any(keyword.lower() in combined_text for keyword in keywords):
            filtered_results.append({
                "Extremophile": extremophile,
                "Resistance_Type": stress_type,
                "Gene": row.get("gene", "Unknown"),
                "Product": row.get("product", "Unknown"),
                "EC_Number": row.get("EC_number", "Unknown"),
                "Locus_ID": row.get("locus_id", "Unknown")
            })
            matched = True
            break

    if not matched:
        filtered_results.append({
            "Extremophile": extremophile,
            "Resistance_Type": "Uncategorized",
            "Gene": row.get("gene", "Unknown"),
            "Product": row.get("product", "Unknown"),
            "EC_Number": row.get("EC_number", "Unknown"),
            "Locus_ID": row.get("locus_id", "Unknown")
        })

# Create DataFrame
filtered_df = pd.DataFrame(filtered_results)

# Save all filtered entries (including Uncategorized)
filtered_df.to_csv(output_all_file, index=False)

# Save only categorized entries
categorized_only_df = filtered_df[filtered_df["Resistance_Type"] != "Uncategorized"]
categorized_only_df.to_csv(output_categorized_file, index=False)

print(f"All filtered entries saved to: {output_all_file}")
print(f"Categorized entries saved to: {output_categorized_file}")
