#!/bin/bash

# List of CORES values to iterate through
CORES_LIST="4 8 12 16 20 24 28 32 36 40"

# Specify the start time in the format YYYY-MM-DDTHH:MM:SS
# START_TIME="2023-11-16T19:39:00"

# Iterate through each value in the list
for CORES in $CORES_LIST; do
    JOB_NAME="job_${CORES}_cores"
    echo "Running SBATCH with $CORES CORES with name $JOB_NAME"
    sbatch --partition=cpar --cpus-per-task=$CORES --output=core_outputs/$JOB_NAME.out scripts/perf.sh
    # sbatch --output=core_outputs/$JOB_NAME.out --partition=cpar --cpus-per-task=$CORES --begin=$START_TIME scripts/perf.sh
    sleep 10
done
