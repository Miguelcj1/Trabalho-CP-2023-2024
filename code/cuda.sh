#!/bin/bash
#SBATCH --time=5:00
#SBATCH --partition=cpar
#SBATCH --constraint=k20

./MDcuda.exe < inputdata.txt
