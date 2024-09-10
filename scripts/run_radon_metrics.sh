#!/bin/bash

# Create the directory for the metrics if it doesn't exist
mkdir -p traces

# File to store the combined radon metrics
output_file="traces/radon_trace.txt"

# Clear previous content from the output file if it exists
> $output_file

echo "Running Radon metrics for the src directory..." | tee -a $output_file

# Cyclomatic Complexity
echo -e "\nCyclomatic Complexity:" | tee -a $output_file
radon cc src -a | tee -a $output_file

# Maintainability Index
echo -e "\nMaintainability Index:" | tee -a $output_file
radon mi src | tee -a $output_file

# Raw Metrics
echo -e "\nRaw Metrics:" | tee -a $output_file
radon raw src | tee -a $output_file

echo -e "\nRadon analysis completed. Metrics saved to $output_file"
