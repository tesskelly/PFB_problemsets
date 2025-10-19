#!/usr/bin/env python3
#1. Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will:
    # INPUT: a string of DNA without newlines
    # OUTPUT: a string of DNA with lines no more than 60 nucleotides long
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
#print(dna)
def dna_sequence(dna):
    seq_list = [] 
    for i in range(0, len(dna), 60):
        sub_dna = dna [i:i+60] 
        #print(sub_dna)
        seq_list.append(sub_dna)
        #print(seq_list)
    dna_sequence = '\n'.join(seq_list)
    return dna_sequence
dna_sequence_return = dna_sequence(dna)
print(dna_sequence_return)








