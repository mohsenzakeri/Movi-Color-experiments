tree_file=$1
# Example: "/home/mzakeri1/vast-blangme2/mzakeri1/bacteria_kraken2/taxonomy/nodes.dmp"

cmd="python find_Pseudomondatoa_taxons.py ${tree_file}"
echo $cmd
eval $cmd

kraken2_fasta=$2
# This should be set to the kraken2 fasta file (library.fna)
# Example: "/home/mzakeri1/vast-blangme2/mzakeri1/bacteria_kraken2/library/bacteria/library.fna"

taxa_ids="all_pseudomanadat.taxa.ids" # Created by find_Pseudomondatoa_taxons.py
kraken2_ids="bacteria_kraken2_library.matching_ids" # output of the next command
cmd="/usr/bin/time grep \"^>\" $kraken2_fasta | awk -F'|' 'NR==FNR {ids[\$1]; next} \
     \$2 in ids' ${taxa_ids} - | cut -f1 -d' ' |  cut -d'>' -f2 > ${kraken2_ids}"
echo $cmd
eval $cmd

cmd="samtools faidx ${kraken2_fasta} \$(cat ${kraken2_ids}) > ${kraken2_ids}.fasta"
echo $cmd
eval $cmd