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

