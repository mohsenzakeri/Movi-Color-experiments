pbsim_path="/vast/blangme2/mzakeri1/softwares/pbsim2/src/pbsim"
hmm_model_path="/vast/blangme2/mzakeri1/softwares/pbsim2/data/R94.model"


mkdir -p simulation_refs
touch simulation_refs/names
touch simulation_refs/names_new


# Select the reference genomes for simulation
for dir in genomes_fasta/*; do

	ls $dir/* | head -n1 >> simulation_refs/names

done

# Move the selected reference genomes to the simulation_refs directory
# The selected reference genomes will not be used for building the index
while IFS= read -r fasta; do

    species=$(echo "$fasta" | sed -E 's/_[0-9]+\.fasta$//' | sed -E 's/genomes_fasta\/[a-zA-Z_]+\///')
    echo $species
    mv  $fasta simulation_refs/$species.fasta

done < simulation_refs/names


# Simulate the reads
read_dir="reads"
mkdir -p $read_dir
while IFS= read -r fasta; do

    species=$(echo "$fasta" | sed -E 's/_[0-9]+\.fasta$//' | sed -E 's/genomes_fasta\/[a-zA-Z_]+\///')
    echo $species

    ref_path="simulation_refs/$species.fasta"
    read_prefix="$read_dir/$species"
    echo $ref_path
    echo $read_prefix

    cmd="$pbsim_path --hmm_model $hmm_model_path --prefix $read_prefix --depth 1 $ref_path > $read_prefix.log 2>&1"
    echo $cmd
    eval $cmd


done < simulation_refs/names

# Create a single fasta file as the main simulated sample from all the reads
# ... (needs t fix read names too)