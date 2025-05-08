# Code written with help from ChatGPT-4

import os
from Bio import Entrez

NUMBER_OF_GENOMES_PER_SPECIES = 100
SPECIES_LIST_FILE_PATH = "species_names_present"

def search_ncbi_genomes(species, count, search_term, output_dir_species):
    # Search the NCBI Genome database
    handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=count)
    record = Entrez.read(handle)
    handle.close()

    genome_ids = record["IdList"]
    print(f"Found {len(genome_ids)} genomes for {species}. Downloading up to {count} genomes in FASTA format.")

    count_genomes = 0
    for genome_id in genome_ids:
        # Fetch genome details in FASTA format
        fasta_handle = Entrez.efetch(db="nucleotide", id=genome_id, rettype="fasta", retmode="text")
        fasta_data = fasta_handle.read()
        fasta_handle.close()

        # Save genome data to a FASTA file
        file_path = os.path.join(output_dir_species, f"{species.replace(' ', '_')}_{genome_id}.fasta")
        with open(file_path, "w") as f:
            f.write(fasta_data)
            count_genomes += 1

        print(f"Saved genome {genome_id} for {species} to {file_path}.")
    
    return count_genomes

def fetch_genomes_fasta(species_list, species_count, output_dir="genomes_fasta"):
    """
    Downloads up to `max_genomes` genomes in FASTA format for a given list of species from NCBI.
    
    Args:
        species_list (list): List of species names.
        output_dir (str): Directory to save the downloaded FASTA files.
        max_genomes (int): Maximum number of genomes to download per species.
    """
    os.makedirs(output_dir, exist_ok=True)

    for species, count in zip(species_list, species_count):
        output_dir_species = output_dir + "/" + species
        output_dir_species = output_dir_species.replace(" ", "_")
        os.makedirs(output_dir_species, exist_ok=True)
        
        print(f"Fetching genomes for: {species}")
        # search_term = f"{species}[Organism] AND (genome)"
        search_term = f'"{species}"[Organism] AND "complete genome"[Title]'

        try:
            count_genomes = search_ncbi_genomes(species, count, search_term, output_dir_species)
            print(f"Fetched {count_genomes} completegenomes for {species}.")
        except Exception as e:
            print(f"Error fetching complete genomes for {species}: {e}")
        if count_genomes < count:
            search_term = f'"{species}"[Organism] NOT "complete genome"[Title]'
            try:
                count_non_complete_genomes = search_ncbi_genomes(species, count - count_genomes, search_term, output_dir_species)
                print(f"Fetched {count_non_complete_genomes} non-complete genomes for {species}.")
            except Exception as e:
                print(f"Error fetching non-complete genomes for {species}: {e}")


if __name__ == "__main__":
    species_list = []
    with open(SPECIES_LIST_FILE_PATH, 'r') as f:
        species_list = [line.strip() for line in f.readlines()]

    species_count = [NUMBER_OF_GENOMES_PER_SPECIES] * len(species_list)   

    fetch_genomes_fasta(species_list, species_count)
