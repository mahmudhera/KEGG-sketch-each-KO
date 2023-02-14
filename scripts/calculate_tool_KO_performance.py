import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("ground_truth_ko_abundance_filename", type=str, help="The full path to the ground truth KO abundance filename. This should be generated by the crete_ko_ground_truth.py script.")
    parser.add_argument("tool_ko_abundance_filename", type=str, help="The full path to the sourmash KO abundance filename. This should be generated by run_sourmash_gather.py, or classify_diamond.py script.")
    parser.add_argument("output_filename", type=str, help="The full path to the performance metrics filename.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    ground_truth_ko_abundance_filename = args.ground_truth_ko_abundance_filename
    tool_ko_abundance_filename = args.tool_ko_abundance_filename
    output_filename = args.output_filename

    # read KO ids from ground truth
    filter_abundances = [ 1.0*i/100 for i in range(11) ]
    df_ground_truth = pd.read_csv(ground_truth_ko_abundance_filename)
    ground_truth_abundance_columns = ['abund_by_num_reads', 'abund_by_nts_covered_in_reads', 'abund_by_mean_cov', 'abund_by_median_cov']

    # read KO ids from the tool output
    df_tool = pd.read_csv(tool_ko_abundance_filename)
    kos_tool_list = df_tool[ 'ko_id' ].tolist()
    kos_tool_set = set(kos_tool_list)

    all_vals_to_write = []
    for filter_abundance in filter_abundances:
        lst = [filter_abundance]
        for ground_truth_abundance_column in ground_truth_abundance_columns:
            # filter KO ids based on the provided filter
            ground_truth_rel_abundances = df_ground_truth[ground_truth_abundance_column].tolist()
            ground_truth_rel_abundances.sort()
            cumulative_abundance = 0.0
            threshold = -1
            for abundance in ground_truth_rel_abundances:
                cumulative_abundance += abundance
                if cumulative_abundance >= filter_abundance:
                    threshold = abundance
                    break
            filtered_df = df_ground_truth[ df_ground_truth[ground_truth_abundance_column] > threshold ]
            filtered_kos_list = filtered_df['ko_id'].tolist()
            filtered_kos_gt_set = set(filtered_kos_list)

            # TP = intersection of these two sets
            # FP = tool_set minus ground_truth_set
            # FN = ground_truth_set minus tool_set
            TP = len(kos_tool_set.intersection(filtered_kos_gt_set))
            FP = len(kos_tool_set.difference(filtered_kos_gt_set))
            FN = len(filtered_kos_gt_set.difference(kos_tool_set))

            recall = 1.0*TP/(TP+FN)
            precision = 1.0*(TP)/(TP+FP)
            try:
                F1 = 2.0/( 1.0/recall + 1.0/precision )
            except:
                F1 = 0.0
            lst.append(precision)
            lst.append(recall)
            lst.append(F1)

        all_vals_to_write.append(lst)

    df_out = pd.DataFrame( all_vals_to_write, columns=['filter_abundance', 'precision_by_num_reads', 'recall_by_num_reads', 'F1_by_num_reads', 'precision_by_nts', 'recall_by_nts', 'F1_by_nts', 'precision_by_mean_cov', 'recall_by_mean_cov', 'F1_by_mean_cov', 'precision_by_med_cov', 'recall_by_med_cov', 'F1_by_med_cov'] )
    df_out.to_csv( output_filename )
