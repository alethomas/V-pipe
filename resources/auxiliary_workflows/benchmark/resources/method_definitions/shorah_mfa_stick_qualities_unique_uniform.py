# GROUP: local
# CONDA: boost = 1.77.0
# CONDA: htslib = 1.14
# CONDA: biopython = 1.79
# PIP: git+https://github.com/LaraFuhrmann/shorah@feature-stick-breaking-quality-score-unique

import subprocess
from pathlib import Path
from os import listdir
from os.path import isfile, join
from Bio import SeqIO
import gzip

def gunzip(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        while True:
            block = s_file.read(block_size)
            if not block:
                break
            else:
                d_file.write(block)


def main(fname_bam, fname_reference, fname_results_snv, fname_result_haplos, dname_work):

    alpha = 0.01
    n_max_haplotypes = 100
    n_mfa_starts = 1

    dname_work.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "shorah",
            "shotgun",
            "-b",
            fname_bam.resolve(),
            "-f",
            fname_reference.resolve(),
            "--inference",
            "mean_field_approximation",
            "--alpha",
            str(alpha),
            "--n_max_haplotypes",
            str(n_max_haplotypes),
            "--n_mfa_starts",
            str(n_mfa_starts),
        ],
        cwd=dname_work,
    )

    (dname_work / "snv" / "SNVs_0.010000_final.vcf").rename(fname_results_snv)
    open(fname_result_haplos, 'a').close()


if __name__ == "__main__":
    main(
        Path(snakemake.input.fname_bam),
        Path(snakemake.input.fname_reference),
        Path(snakemake.output.fname_result),
        Path(snakemake.output.fname_result_haplos),
        Path(snakemake.output.dname_work),
    )
