import argparse
import subprocess
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="This script will take a metagenome as input. Then, it will use exitsing KO sketches (from KEGG database, using FracMinHash) to identify which KO's are found in the metagenome. Mainly, this script is a python wrapper for sourmash gather.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--ksize", type=int, help="k size", default=7)
    parser.add_argument("--seed", type=int, help="Random seed", default=0)
    parser.add_argument("--threshold", type=int, help="sourmash gather threshold bp", default=50)
    parser.add_argument("--metagenome", type=str, help="Full path to the metagenome")
    parser.add_argument("--kosig", type=str, help="Full path to the sketch of the KOs")
    parser.add_argument("--gatherfile", type=str, help="Full path to the gather output filename")
    parser.add_argument("--outfile", type=str, help="Full path to the output KO abundance filename")
    parser.add_argument("--scaled", type=int, help="Scale factor, integer.", default=1000)
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = parse_args()
    ksize = str(args.ksize)
    seed = str(args.seed)
    threshold_bp = str(args.threshold)
    metagenome_file = args.metagenome
    metagenome_name = metagenome_file.split('/')[-1]
    metagenome_path = ''.join(metagenome_file.split('/')[:-1])
    ko_signature_filename = args.kosig
    gather_output_filename = args.gatherfile
    ko_abundance_filename = args.outfile
    scaled = str(args.scaled)
    metagenome_signature_name = metagenome_file + '.sig.zip'
    metagenome_signature_file = metagenome_path + metagenome_signature_name

    cmd = 'sourmash sketch translate -f -p scaled=' + scaled + ',k=' + ksize + ' ' + metagenome_file + ' -o ' + metagenome_signature_file + ' --merge ' + metagenome_signature_file
    subprocess.call( cmd.split(' ') )

    cmd = 'sourmash gather --protein -k ' + ksize + ' --estimate-ani-ci --threshold-bp ' + threshold_bp + ' ' + metagenome_signature_file + ' ' + ko_signature_filename + ' -o ' + gather_output_filename
    subprocess.call( cmd.split(' ') )

    df = pd.read_csv(gather_output_filename, delimiter=',')
    df_new = df[ ['name', 'f_unique_weighted'] ]
    df_new['f_unique_weighted'] = df_new['f_unique_weighted']/df_new['f_unique_weighted'].sum(axis=0)
    df_new.columns = ['koid', 'abundance']
    df_new.to_csv(ko_abundance_filename)
