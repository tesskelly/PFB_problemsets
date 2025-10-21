#!/usr/bin/env python3
# 4. Modify your script so that it can take two command line arguments:
    # FASTA file name
    # Max length of each line

import re
import sys
def dna_sequence(dna,width):
    dna = dna.replace("\n",'')
    seq_list = [] 
    for i in range(0, len(dna), width):
        sub_dna = dna [i:i+width] 
        seq_list.append(sub_dna)
    dna_sequence = '\n'.join(seq_list)
    return dna_sequence

width=int(sys.argv[2])

seq_dict = {}
with open(sys.argv[1]) as python_07_fasta_file: 
    for line in python_07_fasta_file: 
        line = line.strip()
        if line.startswith('>'):
            seq_id = line
            seq = ""
            seq_dict[seq_id]=seq
        else:
            seq_dict[seq_id] += line # += is like .append but for strings
        #print(seq_dict)
for seq_id in seq_dict:
    print(seq_id)

    dna_sequence_return = dna_sequence(seq_dict[seq_id],width)
    print(dna_sequence_return)
