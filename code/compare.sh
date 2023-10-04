#!/bin/bash

# Set the file paths for the three sets of two files
average_base="../documentation/base/cp_average.txt"
average_new="./cp_average.txt"
output_base="../documentation/base/cp_output.txt"
output_new="./cp_output.txt"
traj_base="../documentation/base/cp_traj.xyz"
traj_new="./cp_traj.xyz"

# Compare the first set of files
if cmp -s "$average_base" "$average_new"; then
    echo "cp_average files are the SAME"
else
    echo "cp_average files are DIFFERENT"
fi

# Compare the second set of files
if cmp -s "$output_base" "$output_new"; then
    echo "output_base files are the SAME"
else
    echo "output_base files are DIFFERENT"
fi

# Compare the third set of files
if cmp -s "$traj_base" "$traj_new"; then
    echo "traj_base files are the SAME"
else
    echo "traj_base files are DIFFERENT"
fi