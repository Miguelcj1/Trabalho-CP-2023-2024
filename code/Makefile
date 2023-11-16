CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4
CORES = 12

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

perf:
	sbatch --partition=cpar --cpus-per-task=$(CORES) perf.sh

srun:
	srun --partition=cpar --cpus-per-task=$(CORES) perf stat -e instructions,cycles ./MDpar.exe < inputdata.txt

perfseq:
	srun --partition=cpar perf stat -e instructions,cycles,L1-dcache-load-misses ./MDseq.exe < inputdata.txt

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
	make srun

cmp:
	./cmp.sh
