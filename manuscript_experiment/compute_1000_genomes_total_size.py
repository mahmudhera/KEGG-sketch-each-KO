import os
from Bio import SeqIO

num_selected_genomes = 1000

genome_path = '/scratch/mbr5797/genomes_extracted_from_kegg'
genome_dir_names = [x[0] for x in os.walk(genome_path)][1:]
size_of_genomes = []
for genome_dir in genome_dir_names[:num_selected_genomes]:
    genome_name = genome_dir.split('/')[-1]
    genome_dir_files = [f for f in os.listdir(genome_dir) if os.path.isfile(os.path.join(genome_dir, f))]
    reference_genome = None
    for file in genome_dir_files:
        if file.endswith("fasta"):
            reference_genome = file
            reference_genome_path = os.path.join(genome_dir, reference_genome)
            break
    if reference_genome is None:
        print(f"Could not find reference genome for {genome_name}. Exiting...")
        exit(-1)
    # get the size of the genome as number of nucleotides using SeqIO
    genome_size = 0
    for record in SeqIO.parse(reference_genome_path, 'fasta'):
        genome_size += len(record.seq)
    size_of_genomes.append(genome_size)

print(f"Total size of {num_selected_genomes} genomes: {sum(size_of_genomes)}")
