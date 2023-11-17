CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4
CORES = 20

# .DEFAULT_GOAL = all  #! Mudar para a entrega
.DEFAULT_GOAL = MDpar.exe

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
	rm -f gmon.out grafo.dot
	rm -f slurm*.out

runseq:
	./MDseq.exe < inputdata.txt

runpar:
	./MDpar.exe < inputdata.txt

# Extras

rpar: sbatch

rseq: sbatchseq

sbatch: 
	sbatch --partition=cpar --cpus-per-task=$(CORES) scripts/perf.sh

srun:
	srun --partition=cpar --cpus-per-task=$(CORES) perf stat -e instructions,cycles ./MDpar.exe < inputdata.txt

sbatchseq:
	sbatch --partition=cpar scripts/perf_seq.sh

srunseq:
	srun --partition=cpar perf stat -e instructions,cycles ./MDseq.exe < inputdata.txt

## Faz um sbatch para todas as combinações de cores entre [4..8..40], ficando os outputs armazenados em core_outputs
cores:
	./scripts/cores_test.sh

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
