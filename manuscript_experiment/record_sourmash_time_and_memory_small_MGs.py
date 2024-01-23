import subprocess

script_dir = '../scripts'
python_script = script_dir + '/run_sourmash_gather.py'
threshold_bp = 1000
data_dir = '../data'
scaled = 1000

if __name__ == '__main__':
    # open a file named small_MGs_sourmash_time_and_memory
    # record cpu_time, total_runtime, and maximu_resident_set_size for each run
    # metagenome sizes are 10k, 20k, 30k, 40k, 50k
    # k-mer sizes are 11, 15
    # seed changes from 0 to 9 (total 10)
    # 2 * 5 * 10 = 100 runs in total

    # open file
    file_name = 'small_MGs_sourmash_time_and_memory'
    file = open(file_name, 'w')

    # write header
    file.write('metagenome_size\tkmer_size\tseed\tcpu_time\ttotal_runtime\tmaximum_resident_set_size\n')

    # run sourmash gather
    metagenome_sizes = [10000, 20000, 30000, 40000, 50000]
    kmer_sizes = [11, 15]
    seeds = range(10)
    for metagenome_size in metagenome_sizes:
        for kmer_size in kmer_sizes:
            for seed in seeds:
                # metagenome name format: data_dir/simulated_metagenome_num_reads_xx_seed_yy.fastq
                metagenome_name = data_dir + '/simulated_metagenome_num_reads_' + str(metagenome_size) + '_seed_' + str(seed) + '.fastq'

                # ko sequence bloom filter file name format: "/scratch/mbr5797/KOs_sketched/KOs_sbt_scaled_1000_k_"+str(kmer_size)+".sbt.zip"
                ko_sbt_file_name = "/scratch/mbr5797/KOs_sketched/KOs_sbt_scaled_1000_k_"+str(kmer_size)+".sbt.zip"

                # gather output file name format: data_dir/sourmash_gather_num_reads_xx_seed_yy_k_zz
                gather_output_file_name = data_dir + '/sourmash_gather_num_reads_' + str(metagenome_size) + '_seed_' + str(seed) + '_k_' + str(kmer_size)

                # final output file name format: data_dir/sourmash_kos_xx_seed_yy_k_zz
                final_output_file_name = data_dir + '/sourmash_kos_num_reads_' + str(metagenome_size) + '_seed_' + str(seed) + '_k_' + str(kmer_size)

                # run sourmash gather
                # python run_sourmash_gather.py --ksize kmer_size --threshold threshold_bp --metagenome metagenome_name --kosig kos_sbt_file_name --gatherfile gather_output_file_name --outfile final_output_file_name --scaled scaled
                command = '/usr/bin/time -v python ' + python_script + ' --ksize ' + str(kmer_size) + ' --threshold ' + str(threshold_bp) + ' --metagenome ' + metagenome_name + ' --kosig ' + ko_sbt_file_name + ' --gatherfile ' + gather_output_file_name + ' --outfile ' + final_output_file_name + ' --scaled ' + str(scaled)
                print(command)

                # run command and get stderr output
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                output = output.decode('utf-8')
                output = output.split('\n')

                # user time is at line 23 from the bottom
                # system time is at line 22 from the bottom
                # maximum resident set size is at line 15 from the bottom
                # cpu time is the sum of user time and system time
                # total runtime is the 20th line from the bottom in m:ss format

                # get cpu time, total runtime, maximum resident set size
                cpu_time = float(output[-23].split(' ')[-1]) + float(output[-22].split(' ')[-1])
                total_runtime_string = output[-20].split(' ')[-1]
                total_runtime_seconds = float(total_runtime_string.split(':')[0]) * 60 + float(total_runtime_string.split(':')[1])
                maximum_resident_set_size = int(output[-15].split(' ')[-1])

                # write to file
                file.write(str(metagenome_size) + '\t' + str(kmer_size) + '\t' + str(seed) + '\t' + str(cpu_time) + '\t' + str(total_runtime_seconds) + '\t' + str(maximum_resident_set_size) + '\n')
                file.flush()
    file.close()        