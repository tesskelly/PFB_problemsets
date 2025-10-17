#!/usr/bin/env python3
# Using pattern matching, find all the FASTA header lines in Python_07.fasta.
# Note that the format for a header in a FASTA file is a line that starts with a greater than symbol and is followed by some text
    # ex. (e.g. >seqName description where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)

import re
# with open ('Python_07.fasta.txt','r') as python_07_fasta_file:
#     fasta_content = python_07_fasta_file.readlines() #could you do a for loop instead of .readlines() if you want it to go line by line? 
#     header = (r'^>(\S+)')
#     headers = [line.strip() for line in fasta_content if re.match(header, line)]
#     for line in headers:
#             print(headers)
# don't do this?

with open('Python_07.fasta.txt','r') as python_07_fasta_file: 
    for line in python_07_fasta_file: 
        line = line.strip()
        for found in re.finditer(r'^>(.+)', line):
            print(line)
# this code works, not 100% sure why? 