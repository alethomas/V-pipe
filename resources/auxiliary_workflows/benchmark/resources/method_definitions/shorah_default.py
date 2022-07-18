# GROUP: local
# CONDA: shorah = 1.99.2

import subprocess
from pathlib import Path


def main(fname_bam, fname_reference, fname_result, fname_result_haplos, dname_work):
    dname_work.mkdir(parents=True, exist_ok=True)
    if int(genome_size) < 240:
        open(fname_result, 'a').close()
    else:
        subprocess.run(
            [
                "shorah",
                "shotgun",
                "-b",
                fname_bam.resolve(),
                "-f",
                fname_reference.resolve(),
            ],
            cwd=dname_work,
            check=True,
        )

        open(fname_result_haplos, 'a').close()

if __name__ == "__main__":
    main(
        Path(snakemake.input.fname_bam),
        Path(snakemake.input.fname_reference),
        Path(snakemake.output.fname_result),
        Path(snakemake.output.fname_result_haplos),
        Path(snakemake.output.dname_work),
    )
