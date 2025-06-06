kraken2build="/home/mzakeri1/kraken2/kraken2-2.1.3/kraken2-build"

krakendb="kraken2_custom_db"

# Downloads the taxonomy for the custom database
cmd="$kraken2build --db $krakendb --threads 8 --download-taxonomy"
echo $cmd
eval $cmd

# Add the genomes to the custome database
for fasta in genomes_fasta/*/*.fasta; do
	cmd="$kraken2build --db $krakendb --add-to-library $fasta"
	eval $cmd
done

# Builds the Kraken2 custome databse
cmd="/usr/bin/time $kraken2build --db $krakendb --build --threads 16 > kraken2build.log_time 2>&1"
echo $cmd
eval $cmd
