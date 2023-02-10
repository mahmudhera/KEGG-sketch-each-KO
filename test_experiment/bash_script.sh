#!/usr/bin/env bash
set -e
set -u
scriptDir="../scripts"
dataDir="../data"
resourceDir='../resources'
genomePath="../reference_genomes"

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
echo "$scriptDir/find_genes_in_sim.py --database_dir $genomePath --simulation $simulatedMetagenome --output_file $dataDir/ground_truth.csv"
"$scriptDir/find_genes_in_sim.py --database_dir $genomePath --simulation $simulatedMetagenome --output_file $dataDir/ground_truth.csv"

# summarize to KO level

# run sourmash to find KOs

# find sourmash performance metrics

# Run Diamond
/usr/bin/time $scriptDir/classify_diamond.py -r $proteinDatabaseTruncated -m $simulatedMetagenome -o $dataDir
diamondFile="$dataDir/$(basename $simulatedMetagenome)_$(basename $proteinDatabaseTruncated).dmnd_matches.csv"
echo "diamondFile: $diamondFile"

# summarize to KO level

# find performance metrics

# run kofam scan

# summarize to KO level

# find performance metrics
