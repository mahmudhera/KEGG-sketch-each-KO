#!/usr/bin/env bash
set -e
set -u
scriptDir="../scripts"
dataDir="../data"
resourceDir='../resources'
genomePath="../reference_genomes"

presentGenesFile="../resources/present_genes_and_koids.csv"
koSigFileName="../sketched_references/KOs_sketched_scaled_1000.sig.zip"

genomeDatabaseFull="$dataDir/genome_ref_full.fa"
genomeDatabaseTruncated="$dataDir/genome_ref_truncated.fa"
simulatedMetagenome="$dataDir/simulatedMetagenome.fastq"
proteinDatabaseFull="$dataDir/protein_db_full.fa"
proteinDatabaseTruncated="$dataDir/protein_db_truncated.fa"

numGenomes=5
numGenomesFullDB=$numGenomes
numGenomesTruncatedDB=3

numReads=10000
readLen=150
numGenes=100
kSize=7
refScale=10
queryScale=10
thresholdBP=5000

# create the full genome reference database
echo "$scriptDir/create_genome_ref_db.py $genomePath $genomeDatabaseFull $numGenomesFullDB"
$scriptDir/create_genome_ref_db.py $genomePath $genomeDatabaseFull $numGenomesFullDB

# create the truncated genome reference database
echo "$scriptDir/create_genome_ref_db.py $genomePath $genomeDatabaseTruncated $numGenomesTruncatedDB"
$scriptDir/create_genome_ref_db.py $genomePath $genomeDatabaseTruncated $numGenomesTruncatedDB

# create the protein reference database
echo "$scriptDir/create_gene_ref_db.py "$genomePath" $proteinDatabaseFull $numGenomesFullDB"
$scriptDir/create_gene_ref_db.py "$genomePath" $proteinDatabaseFull $numGenomesFullDB
echo "$scriptDir/create_gene_ref_db.py "$genomePath" $proteinDatabaseTruncated $numGenomesTruncatedDB"
$scriptDir/create_gene_ref_db.py "$genomePath" $proteinDatabaseTruncated $numGenomesTruncatedDB

# simulate a metagenome
echo "$scriptDir/simulate_metagenome.py -r $genomeDatabaseFull -o $simulatedMetagenome -n $numReads -l $readLen --num_orgs $numGenomes"
$scriptDir/simulate_metagenome.py -r $genomeDatabaseFull -o $simulatedMetagenome -n $numReads -l $readLen --num_orgs $numGenomes

# get the abundance estimates for the simulated metagenome
echo $(pwd)
echo "$scriptDir/find_genes_in_sim.py --database_dir $genomePath --simulation $simulatedMetagenome --output_file $dataDir/ground_truth.csv"
python $scriptDir/find_genes_in_sim.py --database_dir $genomePath --simulation $simulatedMetagenome --output_file $dataDir/ground_truth.csv --num_genomes $numGenomesFullDB

# summarize to KO level
echo "$scriptDir/create_ko_ground_truth.py --present_genes $presentGenesFile --gene_abundance $dataDir/ground_truth.csv --out_file $dataDir/ground_truth_ko.csv"
python $scriptDir/create_ko_ground_truth.py --present_genes $presentGenesFile --gene_abundance $dataDir/ground_truth.csv --out_file $dataDir/ground_truth_ko.csv

# run sourmash to find KOs
echo "python $scriptDir/run_sourmash_gather.py --ksize $kSize --threshold $thresholdBP --metagenome $dataDir/simulatedMetagenome.fastq --kosig $koSigFileName --gatherfile $dataDir/sm_gather_output.csv --outfile $dataDir/sourmash_kos.csv --scaled $queryScale"
python $scriptDir/run_sourmash_gather.py --ksize $kSize --threshold $thresholdBP --metagenome $dataDir/simulatedMetagenome.fastq --kosig $koSigFileName --gatherfile $dataDir/sm_gather_output.csv --outfile $dataDir/sourmash_kos.csv --scaled $queryScale

# find sourmash performance metrics for sourmash
echo "python $scriptDir/calculate_tool_KO_performance.py $dataDir/ground_truth_ko.csv $dataDir/sourmash_kos.csv $dataDir/sourmash_performance_metrics.csv"
python $scriptDir/calculate_tool_KO_performance.py $dataDir/ground_truth_ko.csv $dataDir/sourmash_kos.csv $dataDir/sourmash_performance_metrics.csv

# Run Diamond and find KOs
echo "$scriptDir/run_diamond_for_ko.py -r $proteinDatabaseTruncated -m $simulatedMetagenome -o $dataDir -d diamond_output_file.csv -k diamond_kos.csv -p $presentGenesFile"
$scriptDir/run_diamond_for_ko.py -r $proteinDatabaseTruncated -m $simulatedMetagenome -o $dataDir -d diamond_output_file.csv -k diamond_kos.csv -p $presentGenesFile

# find performance metrics for Diamond
echo "python $scriptDir/calculate_tool_KO_performance.py $dataDir/ground_truth_ko.csv $dataDir/diamond_kos.csv $dataDir/diamond_performance_metrics.csv"
python $scriptDir/calculate_tool_KO_performance.py $dataDir/ground_truth_ko.csv $dataDir/diamond_kos.csv $dataDir/diamond_performance_metrics.csv

# run kofam scan
