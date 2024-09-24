#!/bin/bash
#SBATCH --time=10-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem 128000
#SBATCH --partition=long

source ~/.bashrc


export PYTHONPATH="${PYTHONPATH}:/home/lv823975/memory-buffer/Plots"

echo "Number of tasks: "
echo $SLURM_NTASKS


python3 32approximation-8_2.py 

