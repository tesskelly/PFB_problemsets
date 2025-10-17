#!/usr/bin/env python3
import re
with open("Python_07.fasta.txt", "r") as fasta_file:
    for line in fasta_file:
        # Check if the line matches the FASTA header format
        match = re.match(r"^>(\S+)(.*)", line)
        if match:
            # Extract sequence name and description
            seq_name = match.group(1)
            seq_description = match.group(2)
            # Print the extracted information
            print(f"id:{seq_name} desc:{seq_description}")

#the code works!