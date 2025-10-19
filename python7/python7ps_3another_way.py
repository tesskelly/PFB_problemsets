#!/usr/bin/env python3
# If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns (groups).

# import re
# with open('Python_07.fasta.txt','r') as python_07_fasta_file: 
#     for line in python_07_fasta_file: 
#         line = line.strip()
#         for found in re.finditer(r'^>(.+)', line):
#             print(line)

#could also do this
import re #import re function, not included in python
fasta_read = open('Python_07.fasta.txt','r') #open Python_07.fasta.txt and read it as fasta_read variable
fasta = fasta_read.read() 
found_header = re.findall(r'>.+', fasta) #found_header contains all read lines that contain the header format in fasta 
print(found_header) #then print the readout 