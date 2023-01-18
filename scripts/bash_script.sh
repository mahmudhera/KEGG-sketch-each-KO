#!/usr/bin/env bash
set -e
set -u
DATADIR=../data/
OUTDIR=../output/
FILEPREFIX="SRS1041031.denovo_duplicates_marked.trimmed"
SIGFILE=${DATADIR}/${FILEPREFIX}.sig.zip
REF=/data/shared_data/KEGG_data/sourmash_sketches/output_KOs/KOs_sketched/KOs_sketched_scaled_1000.sig.zip
sourmash sketch translate -f -p scaled=1000,k=5 ${DATADIR}/${FILEPREFIX}*.fastq -o ${SIGFILE} --merge ${SIGFILE}
sourmash gather --protein -k 5 --estimate-ani-ci --threshold-bp 500 ${SIGFILE} ${REF} -o ${OUTDIR}/${FILEPREFIX}_$(basename $REF)_gather_k_5.csv
