#!/bin/bash

perf stat -e instructions,cycles ./MDpar.exe < inputdata.txt