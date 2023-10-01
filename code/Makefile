CC = gcc
SRC = src/
CFLAGS = # none

.DEFAULT_GOAL = MD.exe

MD.exe: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) $(SRC)MD.cpp -lm -o MD.exe

clean:
	rm ./MD.exe
	rm cp_average.txt cp_output.txt cp_traj.xyz
	rm gmon.out grafo.dot grafo.png relatorio.txt

run:
	./MD.exe < inputdata.txt

gprof: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) -pg $(SRC)MD.cpp -lm -o MD.exe 

graph:
	gprof MD.exe > relatorio.txt
	gprof2dot -f prof relatorio.txt -o grafo.dot
	dot -Tpng -o grafo.png grafo.dot