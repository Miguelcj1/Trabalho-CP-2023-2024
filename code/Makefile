CC = gcc
SRC = src/
CFLAGS = # none

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

graph:
	gprof MD.exe > ../documentation/relatorio.txt
	gprof2dot -f prof ../documentation/relatorio.txt -o grafo.dot
	dot -Tpng -o ../documentation/grafo.png grafo.dot