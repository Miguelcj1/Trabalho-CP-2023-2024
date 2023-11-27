CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4
THREADS = 40

.DEFAULT_GOAL = all

all: MDseq.exe MDpar.exe

MDseq.exe: $(SRC)/MDseq.cpp
	module load gcc/11.2.0;
	$(CC) $(CFLAGS) $(SRC)MDseq.cpp -lm -o MDseq.exe

MDpar.exe: $(SRC)/MDpar.cpp
	module load gcc/11.2.0;
	$(CC) $(CFLAGS) $(SRC)MDpar.cpp -lm -fopenmp -o MDpar.exe

clean:
	rm -f ./MD*.exe
	rm -f cp_average.txt cp_output.txt cp_traj.xyz

runseq:
	./MDseq.exe < inputdata.txt

runpar:
	export OMP_NUM_THREADS=$(THREADS); ./MDpar.exe < inputdata.txt

# Extras

rpar: sbatch

rseq: sbatchseq

sbatch:
	export OMP_NUM_THREADS=$(THREADS); sbatch --partition=cpar --cpus-per-task=40 scripts/perf.sh;

srun:
	export OMP_NUM_THREADS=$(THREADS); srun --partition=cpar --cpus-per-task=40 perf stat -e instructions,cycles ./MDpar.exe < inputdata.txt;

sbatchseq:
	sbatch --partition=cpar scripts/perf_seq.sh

srunseq:
	srun --partition=cpar perf stat -e instructions,cycles ./MDseq.exe < inputdata.txt

## Faz um sbatch para todas as combinações de threads entre [4..8..40], ficando os outputs armazenados em core_outputs
cores:
	./scripts/cores_test.sh

## Para um numero especifico de cores "make core c=12"
core:
	export OMP_NUM_THREADS=$(c); sbatch --partition=cpar --cpus-per-task=40 --output=core_outputs/job_$(c)_cores.out scripts/perf.sh;

rm_cores:
	rm core_outputs/job_*_cores.out

rm_slurm:
	rm -f slurm*.out


gprof: $(SRC)/MDpar.cpp
	$(CC) $(CFLAGS) -pg $(SRC)MDpar.cpp -lm -fopenmp -o MDpar.exe 

graph:
	gprof MDpar.exe > relatorio.txt
	gprof2dot -f prof relatorio.txt -o grafo.dot
	dot -Tpng -o grafo.png grafo.dot

scp:
	scp cp:Trabalho-CP-2023-2024/code/gmon.out .
	scp cp:Trabalho-CP-2023-2024/code/MDpar.exe .

re:
	make clean
	make MDpar.exe
	make perf

cmp:
	./scripts/cmp.sh
