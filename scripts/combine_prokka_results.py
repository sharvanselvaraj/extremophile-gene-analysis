import os
import pandas as pd

# Define paths
prokka_input_dir = "../data"
output_file = "../data/combined_prokka.csv"

# Columns of interest from Prokka annotations
columns_of_interest = ["locus_id", "gene", "product", "EC_number"]

# Function to parse Prokka .gff files
def parse_prokka_gff(file_path, extremophile_name):
    prokka_data = []
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                parts = line.strip().split("\t")
                if len(parts) >= 9:
                    attributes = parts[8]
                    data = {"locus_id": parts[0], "gene": None, "product": None, "EC_number": None}
                    for attribute in attributes.split(";"):
                        if "=" in attribute:
                            key, value = attribute.split("=", 1)
                            if key == "gene":
                                data["gene"] = value
                            elif key == "product":
                                data["product"] = value
                            elif key.lower() == "ec_number" or key.lower() == "eC_number":
                                data["EC_number"] = value
                    data["extremophile"] = extremophile_name
                    prokka_data.append(data)
    return pd.DataFrame(prokka_data)

# Parse all Prokka .gff files and consolidate
all_data = []
for file_name in os.listdir(prokka_input_dir):
    if file_name.endswith(".gff"):
        file_path = os.path.join(prokka_input_dir, file_name)
        extremophile_name = file_name.split("_")[0]  # Extract extremophile name from filename
        prokka_df = parse_prokka_gff(file_path, extremophile_name)
        all_data.append(prokka_df)

# Combine all data into a single DataFrame
if all_data:  # Ensure there's data to combine
    combined_df = pd.concat(all_data, ignore_index=True)
    # Save to CSV
    combined_df.to_csv(output_file, index=False)
    print(f"Consolidated Prokka data saved to: {output_file}")
else:
    print("No valid Prokka GFF files found.")
