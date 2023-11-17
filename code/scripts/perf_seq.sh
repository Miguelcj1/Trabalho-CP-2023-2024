#!/bin/bash

perf stat -e instructions,cycles ./MDseq.exe < inputdata.txt