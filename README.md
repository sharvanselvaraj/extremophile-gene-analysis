# Extremophile Stress Resistance Gene Function Analysis

A bioinformatics pipeline to analyze and compare stress resistance gene function across five extremophile organisms using genome annotation, stress gene categorization, and network analysis.

---

## Background

The initial goal of this project was ambitious — to predict which extremophile organism would have the highest probability of surviving on Mars, using machine learning trained on real Martian environmental data from NASA's REMS instrument on the Curiosity rover.

To achieve that, we first needed to quantify the stress resistance capability of each organism at the genomic level. This pipeline was built to do exactly that — systematically identify, categorize, and score stress resistance genes across five extremophiles using genome annotation and network analysis.

While the Mars survival prediction model remains a work in progress due to challenges in obtaining a clean and reliable Martian environmental dataset, the gene function analysis pipeline is complete and produces meaningful biological insights in its own right.

---

## Organisms Studied

| Organism | Extreme Condition |
|---|---|
| *Deinococcus radiodurans* | Radiation resistance |
| *Halobacterium salinarum* | Salt tolerance |
| *Psychrobacter spp.* | Cold resistance |
| *Acidithiobacillus ferrooxidans* | Acidic environment adaptation |
| *Thermus aquaticus* | Heat resistance |

---

## Pipeline Overview
```
Genome sequences (NCBI)
↓
Genome annotation — PROKKA + RAST
↓
Annotation parsing and merging
↓
Stress resistance gene filtering and categorization
↓
Gene feature encoding and survival scoring
↓
Visualization — heatmaps, radar plots, clustering, rankings
↓
Network analysis — gene to resistance category connections
```

---

## Repository Structure

```
extremophile-gene-analysis/
│
├── data/                        
│   ├── *_prokka.gff             
│   ├── *_RAST.xls               
│   ├── combined_prokka.csv      
│   ├── combined_RAST.csv        
│   └── ...                      
│
├── scripts/                     
│   ├── combine_prokka_results.py
│   ├── combine_rast_results.py
│   ├── combine_prokka_rast.py
│   ├── filter_stress_responsive_genes.py
│   ├── encode_gene_features.py
│   ├── compute_survival_scores.py
│   ├── visualize_heatmap.py
│   ├── visualize_clustering.py
│   ├── visualize_radar_plots.py
│   ├── visualize_rankings.py
│   ├── clean_stress_genes.py
│   ├── build_network_graph.py
│   ├── compute_network_metrics.py
│   └── summarize_gene_functions.py
│
├── outputs/                     
│   ├── extremophile_resistance_heatmap.png
│   ├── extremophile_clusters_heatmap.png
│   ├── *_radar_plot.png         
│   ├── resistance_score_barplot.png
│   ├── enhanced_gene_function_network_spread2.png
│   ├── top_gene_products_by_stress_type.png
│   ├── extremophile_resistance_scores.csv
│   └── network_metrics.csv
│
└── README.md
```

---

## How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn networkx requests xlwings
```

### External Tools
- **PROKKA** — genome annotation. Install via conda: `conda install -c bioconda prokka`
- **RAST** — web-based annotation available at [rast.nmpdr.org](https://rast.nmpdr.org)

### Genome Data
Genome sequences were downloaded from NCBI. Run PROKKA on each genome to reproduce the GFF annotation files used as pipeline input.

### Running the Pipeline
Run scripts in order from the `scripts/` directory:

```bash
python combine_prokka_results.py
python combine_rast_results.py
python combine_prokka_rast.py
python filter_stress_responsive_genes.py
python encode_gene_features.py
python compute_survival_scores.py
python visualize_heatmap.py
python visualize_clustering.py
python visualize_radar_plots.py
python visualize_rankings.py
python clean_stress_genes.py
python build_network_graph.py
python compute_network_metrics.py
python summarize_gene_functions.py
```

---

## Results

### Stress Resistance Rankings
| Rank | Organism | Resistance Score |
|---|---|---|
| 1 | *Psychrobacter spp.* | 114 |
| 2 | *Deinococcus radiodurans* | 112 |
| 3 | *Acidithiobacillus ferrooxidans* | 106 |
| 4 | *Thermus aquaticus* | 94 |
| 5 | *Halobacterium salinarum* | 76 |

### Key Finding
Network centrality analysis revealed radiation resistance as the most interconnected stress response category (degree: 132, betweenness: 0.238), consistent with *Deinococcus radiodurans* being one of the most radiation resistant organisms known.

### Visualizations

**Stress Resistance Heatmap**
![Heatmap](outputs/extremophile_resistance_heatmap.png)

**Gene-Resistance Network Graph**
![Network](outputs/enhanced_gene_function_network_spread2.png)

---

## Future Work

- Complete KEGG pathway mapping to enrich gene functional annotations
- Expand the analysis to include additional extremophile organisms
- Obtain a reliable Martian environmental dataset (NASA REMS) to build the originally intended ML model predicting extremophile survival probability under Martian conditions
- Apply graph neural networks to the gene-resistance network for deeper functional prediction
- Explore transfer learning approaches to generalize survival predictions to other extreme planetary environments

---

## Dependencies

| Library | Purpose |
|---|---|
| pandas | Data manipulation |
| numpy | Numerical computing |
| matplotlib | Visualization |
| seaborn | Statistical visualization |
| scikit-learn | Machine learning and preprocessing |
| networkx | Network graph analysis |
| requests | KEGG API queries |
| xlwings | Excel file handling |
| PROKKA | Genome annotation (external) |
| RAST | Genome annotation (external) |
