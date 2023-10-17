CC = gcc
SRC = src/
# CFLAGS = -O2
# CFLAGS = -O2 -funroll-loops
# CFLAGS = -O3
CFLAGS = -O3 -ftree-vectorize -msse4 -fno-omit-frame-pointer


.DEFAULT_GOAL = MD.exe

MD.exe: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) $(SRC)MD.cpp -lm -o MD.exe

clean:
	rm -f ./MD.exe
	rm -f cp_average.txt cp_output.txt cp_traj.xyz
	rm -f gmon.out grafo.dot

run:
	./MD.exe < inputdata.txt

gprof: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) -pg $(SRC)MD.cpp -lm -o MD.exe 

perf:
	srun --partition=cpar perf stat -e instructions,cycles,L1-dcache-load-misses ./MD.exe < inputdata.txt

graph:
	gprof MD.exe > relatorio.txt
	gprof2dot -f prof relatorio.txt -o grafo.dot
	dot -Tpng -o grafo.png grafo.dot


# Extra make commands
scp:
	scp cp:Trabalho-CP-2023-2024/code/gmon.out .
	scp cp:Trabalho-CP-2023-2024/code/MD.exe .

cmp:
	./cmp.sh

re:
	make clean
	make MD.exe
	make perf