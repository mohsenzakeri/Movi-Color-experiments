# Movi-in-Color-experiments


## Building the 48-species dataset

### 1. Download genomes for all species

Once you are in the main directory of the repository, run the following command to download the genomes:

```bash
python fetch_genomes.py
```

Genomes will be saved in the `genomes_fasta` directory.

### 2. Simulate reads from one genome per species (excluded from the index)

You will first need to install [PBSIM2](https://github.com/yukiteruono/pbsim2) software for simulating the reads.

Then, set the following variables at the beginning of the `simulate.sh`:

- `pbsim_path`: path to the PBSIM2 binary

- `hmm_model_path`: path to the error model file (e.g., **R94.model**)

Then, from the main directory of the repository run:

```bash 
bash simulate.sh
```

The simulated reads will be located in a directory called `reads`. The specific genomes used for the simulation will be at `simulation_refs`. These genomes will be removed from the `genomes_fasta` directory after running the simulation.

## Building the _Pseudomonadota_ dataset

### 1. Build a Kraken2 library
First, build a [Krake2](https://github.com/DerrickWood/kraken2/wiki/Manual) library on all complete genomes from Bacteria:
```
kraken2-build --download-taxonomy --db <DBNAME>
kraken2-build --download-library bacteria --db <DBNAME>
```
`DBNAME` is the address of where the Kraken2 library will be located.

### 2. Obtain the genomes from the Kraken2 library
Then, run the following to build a fasta that only includes the `Pseudomonadota` entries found in the Kraken2 library:

Note: The following step requires [samtools](https://www.htslib.org/) to be completed.
```
 bash create_Pseudomonadota_fasta.sh <DBNAME>/taxonomy/nodes.dmp <DBNAME>/library/bacteria/library.fna
```
The first argument is the taxonomy tree downloaded by Kraken2, and the second argument is the fasta including all the complete bacteria genomes in the Kraken2 library.
The resulting new fasta will be named `bacteria_kraken2_library.matching_ids.fasta`.
