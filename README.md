# KEGG-sketch-each-KO
This repository implements the 'sketch each KO' approach to perform functional
annotation on KEGG data using FracMinHash. The KO sketches are already precomputed by
David, and this repository is simply using those. Long term plans:

1. Add code to compute KofamSCAN results.
1. Add code to get TP TN etc.
1. Add code to visualize these.
1. Add snakefile.

Running kofam-scan: exec_annotation -o kofamscan_result simulatedMetagenome.fastq

## Installation
```
conda create -y --name annotate_ko
conda install -y --name annotate_ko -c conda-forge -c bioconda --file requirements.txt
conda activate annotate_ko
```

## How to run?
After installing, we need to do the following:
1. Change stuff in a snakefile (customize to whatever experiment we want to run)
1. Then, `snakemake create_all_metagenomes -j <num_cores_to_use>`
1. Then, `snakemake create_all_ko_ground_truths -j <num_cores_to_use>`
1. Then, `snakemake all -j <num_cores_to_use>`
