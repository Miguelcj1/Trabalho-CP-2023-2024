#!/bin/bash

perf stat -e instructions,cycles,LLC-loads ./MDseq.exe < inputdata.txt