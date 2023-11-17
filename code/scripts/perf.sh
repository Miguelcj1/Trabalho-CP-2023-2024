#!/bin/bash

perf stat -e instructions,cycles,LLC-loads ./MDpar.exe < inputdata.txt