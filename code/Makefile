CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4
THREADS = 40
CUDAFLAGS = -O2 -std=c++11 -arch=sm_35 -Wno-deprecated-gpu-targets

.DEFAULT_GOAL = all

#! Makefile: MDcuda.exe
all: MDseq.exe MDpar.exe MDcuda.exe

MDseq.exe: $(SRC)/MDseq.cpp
	module load gcc/11.2.0;\
	$(CC) $(CFLAGS) $(SRC)MDseq.cpp -lm -o MDseq.exe

MDpar.exe: $(SRC)/MDpar.cpp
	module load gcc/11.2.0;\
	$(CC) $(CFLAGS) $(SRC)MDpar.cpp -lm -fopenmp -o MDpar.exe

MDcuda.exe: $(SRC)/MDcuda.cu
	module load gcc/7.2.0;\
    module load cuda/11.3.1;\
    nvcc $(CUDAFLAGS) $(SRC)MDcuda.cu -o MDcuda.exe

clean:
	rm -f ./MD*.exe
	rm -f cp_average.txt cp_output.txt cp_traj.xyz

rm_sl:
	rm -f slurm*.out

runseq:
	./MDseq.exe < inputdata.txt

runpar:
	export OMP_NUM_THREADS=$(THREADS); ./MDpar.exe < inputdata.txt

run:
	module load gcc/7.2.0;\
    module load cuda/11.3.1;\
	sbatch ./cuda.sh

ccu: MDcuda.exe 

cmp:
	./scripts/cmp.sh
