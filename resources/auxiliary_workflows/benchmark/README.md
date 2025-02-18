# Quasispecies Reconstruction Benchmark

Benchmark Quasispecies assembly methods both on the level of local as well as global haplotypes.

## Usage

To run the workflow, execute the following:

```bash
# locally (remove docker part if on linux)
docker run --rm -v $PWD:/foo --workdir=/foo snakemake/snakemake:stable snakemake -prj1 --use-conda

# on cluster
./run_workflow.sh
```

## Adding new methods

To run a new method/tool as part of the benchmark workflow, add a script to `resources/method_definitions/`.
Each script must be classified as either `local` (produces a VCF file) or global (produces a FASTA file) by adding `# GROUP: local` or `# GROUP: global` respectively.
Method dependencies can be specified as comments.
Conda packages can be added by writing `# CONDA: <package name> = <version>`.
Analogously, PIP packages can be added by writing `# PIP: <package name>`.
Multiple packages can be added by repeating these lines.
A conda environment will then be dynamically generated (when running Snakemake with `--use-conda`).
