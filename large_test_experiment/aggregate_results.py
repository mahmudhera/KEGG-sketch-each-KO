import numpy as np

script_dir = '../../scripts'
data_dir = 'data'
read_length = 150
k = 7
ref_scale = 10
query_scale = 1
threshold_bp = 50
num_organisms = 30
num_genomes_full_db = 30
num_genomes_truncated_db = 20
num_reads_list=['50000', '100000', '150000']
#num_reads_list = ['250000', '500000', '750000', '1000000', '1250000', '1500000', '1750000', '2000000']
#num_reads_list = ['1000000', '1500000', '2000000']
seeds_list = [str(i) for i in range(20)]
kmer_sizes = ['5', '7', '11', '15']

line_num_to_read = 6


def get_diamond_running_time(num_reads, seed):
    filename = data_dir+f'/diamond_benchmark_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()

    time_1 = float(all_lines[1].split('\t')[0])
    #time_2 = float(all_lines[2].split('\t')[0])
    #time_3 = float(all_lines[3].split('\t')[0])

    #all_times = [time_1, time_2, time_3]

    #return float( sum(all_times) - max(all_times) - min(all_times) )

    return time_1

def get_all_diamond_running_times(num_reads):
    return [ get_diamond_running_time(num_reads, seed) for seed in seeds_list ]

def get_sourmash_running_time(num_reads, ksize, seed):
    filename = data_dir + f"/sourmash_gather_benchmark_{num_reads}_seed_{seed}_k_{ksize}"
    f = open(filename, 'r')
    all_lines = f.readlines()
    f.close()

    time_1 = float(all_lines[1].split('\t')[0])
    #time_2 = float(all_lines[2].split('\t')[0])
    #time_3 = float(all_lines[3].split('\t')[0])

    #all_times = [time_1, time_2, time_3]

    #return float( sum(all_times) - max(all_times) - min(all_times) )
    return time_1

def get_all_sourmash_running_times(num_reads, ksize):
    return [get_sourmash_running_time(num_reads, ksize, seed) for seed in seeds_list]

def get_diamond_precision(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[2]
    f.close()
    return float(prec_str)

def get_diamond_recall(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[3]
    f.close()
    return float(prec_str)

def get_diamond_F1(num_reads, seed):
    filename = data_dir+f'/diamond_performance_metrics_num_reads_{num_reads}_seed_{seed}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[4]
    f.close()
    return float(prec_str)

def get_sourmash_precision(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[2]
    f.close()
    return float(prec_str)

def get_sourmash_recall(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[3]
    f.close()
    return float(prec_str)

def get_sourmash_F1(num_reads, seed, k):
    filename = data_dir+f'/sourmash_performance_metrics_num_reads_{num_reads}_seed_{seed}_k_{k}'
    f = open(filename, 'r')
    prec_str = f.readlines()[line_num_to_read].split(',')[4]
    f.close()
    return float(prec_str)


if __name__ == "__main__":
    print('Precisions:')

    for num_reads in num_reads_list:
        res = [get_diamond_precision(num_reads, seed) for seed in seeds_list]
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
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_F1(num_reads, seed, k) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')

    print('Time to run the tools:')
    for num_reads in num_reads_list:
        res = [get_diamond_running_time(num_reads, seed) for seed in seeds_list]
        print(np.mean(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_running_time(num_reads, k, seed) for seed in seeds_list]
            print(np.mean(res), end = ' ')
        print('')

    print('StdDev of time to run the tools:')
    for num_reads in num_reads_list:
        res = [get_diamond_running_time(num_reads, seed) for seed in seeds_list]
        print(np.std(res), end = ' ')
    print('')
    for k in kmer_sizes:
        for num_reads in num_reads_list:
            res = [get_sourmash_running_time(num_reads, k, seed) for seed in seeds_list]
            print(np.std(res), end = ' ')
        print('')
