#!/usr/bin/env python3
# 1. The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotides.
# 2. See the IUPAC table to identify the nucleotide possibilities for the R and Y.
# 3. Write a regular expression to find and print all occurrences of the site in the following sequence Python_07_ApoI.fasta.
# 4. (Just in case you were wondering: The '^' in R^AATTY is NOT actually part of the pattern.
# 5. It just indicates where the cut is happening.)

import re
with open ('Python_07_ApoI.fasta','r') as python_07_ApoI_fasta_file:
    for line in python_07_ApoI_fasta_file: 
        line = line.strip()
        for found in re.findall(r'(A)AATT(G))', line):
            print(line)

