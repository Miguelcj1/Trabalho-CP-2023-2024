CC = gcc
SRC = src/
CFLAGS = -O2 -ftree-vectorize -msse4


.DEFAULT_GOAL = MD.exe

MD.exe: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) $(SRC)MD.cpp -lm -o MD.exe

clean:
	rm -f ./MD.exe

run:
	./MD.exe < inputdata.txt