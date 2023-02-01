# KEGG-sketch-each-KO
This repository implements the 'sketch each KO' approach to perform functional
annotation on KEGG data using FracMinHash. The KO sketches are already precomputed by
David, and this repository is simply using those. Long term plans:

1. Add code to compute the ground truth KO abundance.
1. Add code to compute KofamSCAN results.
1. Add code to compare these.
1. Add code to visualize these.
1. Add snakefile.
