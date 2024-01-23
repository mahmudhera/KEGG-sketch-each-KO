import numpy as np
import pandas as pd

data_dir = 'data_small_sized_metagenomes'

read_length = 150
ref_scale = 1000
query_scale = 1000
threshold_bp = 5
num_organisms = 1000
num_genomes_full_db = 1000
num_genomes_truncated_db = 1000
num_reads_list = [str((i+1)*10000) for i in range(5)]
#num_reads_list = [str((i+1)*1000000) for i in range(5)]
seeds_list = [str(i) for i in range(10)]
kmer_sizes = [str(ksize) for ksize in [11, 15] ]
k = 11
pident_threshold = 0.1 # used in Diamond


# sorting relative abundances from high to low, report top 95% KOs that has been reported
# top 100%: line 2
# top 99%: line 3
# top 98%: line 4
# top 97%: line 5
# top 96%: line 6
# top 95%: line 7
line_number = 7


def get_sourmash_memory(num_reads, ksize, seed):
    filename = 'small_MGs_sourmash_time_and_memory'
    # read the file as pandas dataframe
    df = pd.read_csv(filename, sep='\t')
    # filter the dataframe
    df = df[(df['metagenome_size'] == int(num_reads)) & (df['kmer_size'] == int(ksize)) & (df['seed'] == int(seed))]
    # get the maximum resident set size
    max_resident_set_size = df['maximum_resident_set_size'].values[0]
    return max_resident_set_size/(1024.0*1024.0)


def get_kofam_memory(num_reads, seed):
    filename = data_dir+f'/kofam_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    mem_mb = float(all_lines[1].split('\t')[2])

    return mem_mb/1024.0


def get_diamond_memory(num_reads, seed):
    filename = data_dir+f'/diamond_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    mem_mb = float(all_lines[1].split('\t')[2])

    return mem_mb/1024.0


def get_diamond_running_time(num_reads, seed):
    filename = data_dir+f'/diamond_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    time_1 = float(all_lines[1].split('\t')[0])

    return time_1

def get_kofam_running_time(num_reads, seed):
    filename = data_dir+f'/kofam_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    time_1 = float(all_lines[1].split('\t')[0])

    return time_1

def get_all_diamond_running_times(num_reads):
    return [ get_diamond_running_time(num_reads, seed) for seed in seeds_list ]

def get_kofam_cpu_time(num_reads, seed):
    filename = data_dir+f'/kofam_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    cpu_time = float(all_lines[1].split('\t')[9])
    return cpu_time

def get_diamond_cpu_time(num_reads, seed):
    filename = data_dir+f'/diamond_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()
    try:
        cpu_time = float(all_lines[1].split('\t')[9])
    except:
        print(num_reads, seed)
        print(all_lines[1].split('\t'))
        exit(-1)
    return cpu_time

def get_sourmash_cpu_time(num_reads, ksize, seed):
    filename = 'small_MGs_sourmash_time_and_memory'
    # read the file as pandas dataframe
    df = pd.read_csv(filename, sep='\t')
    # filter the dataframe
    df = df[(df['metagenome_size'] == int(num_reads)) & (df['kmer_size'] == int(ksize)) & (df['seed'] == int(seed))]
    # get the cpu time
    cpu_time = df['cpu_time'].values[0]
    return cpu_time


def get_sourmash_running_time(num_reads, ksize, seed):
    filename = 'small_MGs_sourmash_time_and_memory'
    # read the file as pandas dataframe
    df = pd.read_csv(filename, sep='\t')
    # filter the dataframe
    df = df[(df['metagenome_size'] == int(num_reads)) & (df['kmer_size'] == int(ksize)) & (df['seed'] == int(seed))]
    # get the total runtime
    total_runtime = df['total_runtime'].values[0]
    return total_runtime


def get_diamond_precision(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[2]
    f.close()
    return float(prec_str)

def get_diamond_recall(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[3]
    f.close()
    return float(prec_str)

def get_diamond_F1(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[4]
    f.close()
    return float(prec_str)

def get_sourmash_precision(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[2]
    f.close()
    return float(prec_str)

def get_sourmash_recall(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[3]
    f.close()
    return float(prec_str)

def get_sourmash_F1(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[4]
    f.close()
    return float(prec_str)

def get_kofam_precision(num_reads, seed):
    filename = data_dir+f'/kofam_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[2]
    f.close()
    return float(prec_str)

def get_kofam_recall(num_reads, seed):
    filename = data_dir+f'/kofam_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[3]
    f.close()
    return float(prec_str)

def get_kofam_F1(num_reads, seed):
    filename = data_dir+f'/kofam_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_number-1].split(',')[4]
    f.close()
    return float(prec_str)

if __name__ == "__main__":
    print('Precisions:')

    for num_reads in num_reads_list:
        res = [get_diamond_precision(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_precision(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_precision(num_reads, seed, k) for seed in seeds_list]
            print(np.mean(res), end = ' ')
        print('')

    print('Precision std. devs:')

    for num_reads in num_reads_list:
        res = [get_diamond_precision(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_precision(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_precision(num_reads, seed, k) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')

    print('Recalls:')

    for num_reads in num_reads_list:
        res = [get_diamond_recall(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_recall(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_recall(num_reads, seed, k) for seed in seeds_list]
            print(np.mean(res), end = ' ')
        print('')

    print('Recall std. devs:')

    for num_reads in num_reads_list:
        res = [get_diamond_recall(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_recall(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_recall(num_reads, seed, k) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')

    print('F1 scores:')

    for num_reads in num_reads_list:
        res = [get_diamond_F1(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_F1(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_F1(num_reads, seed, k) for seed in seeds_list]
            print(np.mean(res), end = ' ')
        print('')

    print('F1 std. devs:')

    for num_reads in num_reads_list:
        res = [get_diamond_F1(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_F1(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_F1(num_reads, seed, k) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')

    print('CPU Time to run the tools: (log10 of seconds)')
    for num_reads in num_reads_list:
        res = [get_diamond_cpu_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.mean(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_cpu_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_cpu_time(num_reads, k, seed) for seed in seeds_list]
            res = np.log(res) / np.log(10)
            print(np.mean(res), end = ' ')
        print('')

    print('StdDev of cpu time to run the tools:')
    for num_reads in num_reads_list:
        res = [get_diamond_cpu_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_cpu_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_cpu_time(num_reads, k, seed) for seed in seeds_list]
            res = np.log(res) / np.log(10)
            print(np.std(res), end = ' ')
        print('')

    print('Running time of all tools (in logarithm of seconds):')
    for num_reads in num_reads_list:
        res = [get_diamond_running_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.mean(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_running_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_running_time(num_reads, k, seed) for seed in seeds_list]
            res = np.log(res) / np.log(10)
            print(np.mean(res), end = ' ')
        print('')


    print('Stddev of running time of all tools (in logarithm of seconds):')
    for num_reads in num_reads_list:
        res = [get_diamond_running_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_running_time(num_reads, seed) for seed in seeds_list]
        res = np.log(res) / np.log(10)
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_running_time(num_reads, k, seed) for seed in seeds_list]
            res = np.log(res) / np.log(10)
            print(np.std(res), end = ' ')
        print('')
        

    print('Memory usage (in GB):')
    for num_reads in num_reads_list:
        res = [get_diamond_memory(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ') 
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_memory(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_memory(num_reads, k, seed) for seed in seeds_list]
            print(np.mean(res), end = ' ')
        print('')

    print('Stddev of memory usage (in GB):')
    for num_reads in num_reads_list:
        res = [get_diamond_memory(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for num_reads in num_reads_list:
        res = [get_kofam_memory(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_memory(num_reads, k, seed) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')

