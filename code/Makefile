CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4

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

runseq:
	./MDseq.exe < inputdata.txt

runpar:
	./MDpar.exe < inputdata.txt

perf:
	srun --partition=cpar perf stat -e instructions,cycles,L1-dcache-load-misses ./MDpar.exe < inputdata.txt

perfseq:
	srun --partition=cpar perf stat -e instructions,cycles,L1-dcache-load-misses ./MDseq.exe < inputdata.txt


re:
	make clean
	make MDpar.exe
	make perf