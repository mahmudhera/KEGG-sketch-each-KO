import argparse
import pandas as pd

def parse_args(): # pragma: no cover
    parser = argparse.ArgumentParser(description="This script will take a list of <gene_id, ko_id> mapping, and also take the gene abundance information in a simulation. Then, this script will summarize the abundane information from gene level to KO level.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--present_genes', type=str, help='file containing list of present genes and KO ids. Generated by main.py of the repo: https://github.com/mahmudhera/extract-kegg-organisms')
    parser.add_argument('--gene_abundance', type=str, help='file containing gene abundance information of a simulation. Generated by the script find_genes_in_sim.py of the repo: https://github.com/mahmudhera/KEGG_sketching_annotation')
    parser.add_argument('--out_file', type=str, help='file that will contain ko level abundance information.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    present_genes_filename = args.present_genes
    gene_abundance_filename = args.gene_abundance
    output_filename = args.out_file

    gene_abundance_df = pd.read_csv(gene_abundance_filename)
    gene_names = gene_abundance_df['gene_name'].tolist()
    gene_lengths = gene_abundance_df['gene_length'].tolist()
    nt_ovelaps = gene_abundance_df['nucleotide_overlap'].tolist()
    list_reads_mapped = gene_abundance_df['reads_mapped'].tolist()
    num_bases_of_the_gene_covered = gene_abundance_df['num_nts_in_reads'].tolist()
    mean_coverages = gene_abundance_df['mean_coverage'].tolist()
    median_coverages = gene_abundance_df['median_coverage'].tolist()

    gene_koid_df = pd.read_csv(present_genes_filename)
    gene_ids = gene_koid_df['gene_id'].tolist()
    ko_ids = gene_koid_df['ko_id'].tolist()

    gene_id_to_ko_id = {}
    for gene_id, ko_id in list( zip(gene_ids, ko_ids) ):
        gene_id_to_ko_id[gene_id] = ko_id

    total_num_reads = sum(list_reads_mapped)
    total_nucleotides_covered = sum(nt_ovelaps)
    total_bases_of_the_gene_covered_by_reads = sum(num_bases_of_the_gene_covered)
    sum_mean_coverage = sum(mean_coverages)
    sum_median_coverag = sum(median_coverages)

    ko_abundances_by_num_reads = {}
    ko_abundances_by_num_nts_in_reads = {}
    ko_abundances_by_mean_cov = {}
    ko_abundances_by_med_cov = {}

    for gene_id, gene_length, nt_overlap, num_reads_mapped, num_bases_covered, mean_cov, med_cov in list( zip(gene_names, gene_lengths, nt_ovelaps, list_reads_mapped, num_bases_of_the_gene_covered, mean_coverages, median_coverages) ):
        abundance_estimate_1 = 1.0 * num_reads_mapped / total_num_reads
        abundance_estimate_2 = 1.0 * nt_overlap / total_nucleotides_covered
        abundance_estimate_3 = 1.0 * num_bases_covered / total_bases_of_the_gene_covered_by_reads
        abundance_estimate_4 = 1.0 * mean_cov / sum_mean_coverage
        abundance_estimate_5 = 1.0 * med_cov / sum_median_coverag

        ko_id = gene_id_to_ko_id[gene_id]
        if ko_id in ko_abundances_by_num_reads.keys():
            ko_abundances_by_num_reads[ko_id] += abundance_estimate_1
            ko_abundances_by_num_nts_in_reads[ko_id] += abundance_estimate_3
            ko_abundances_by_mean_cov[ko_id] += abundance_estimate_4
            ko_abundances_by_med_cov[ko_id] += abundance_estimate_5
        else:
            ko_abundances_by_num_reads[ko_id] = abundance_estimate_1
            ko_abundances_by_num_nts_in_reads[ko_id] = abundance_estimate_3
            ko_abundances_by_mean_cov[ko_id] = abundance_estimate_4
            ko_abundances_by_med_cov[ko_id] = abundance_estimate_5

    out_list = []
    for ko_id in ko_abundances_by_num_reads.keys():
        out_list.append((ko_id, ko_abundances_by_num_reads[ko_id], ko_abundances_by_num_nts_in_reads[ko_id], ko_abundances_by_mean_cov[ko_id], ko_abundances_by_med_cov[ko_id]))

    out_df = pd.DataFrame(out_list, columns=['ko_id', 'abund_by_num_reads', 'abund_by_nts_covered_in_reads', 'abund_by_mean_cov', 'abund_by_median_cov'])
    out_df.to_csv( output_filename )