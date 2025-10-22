#!/usr/bin/env python3
#!/usr/bin/env python3
#2. Modify your function so that it will work whether the DNA string does or does not have newlines.
import re
dna_string = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

def dna_sequence(dna):
    dna = dna.replace("\n",'')
    seq_list = [] 
    for i in range(0, len(dna), 60):
        sub_dna = dna [i:i+60] 
        seq_list.append(sub_dna)
    dna_sequence = '\n'.join(seq_list)
    return dna_sequence

dna_sequence_return = dna_sequence(dna_string)
print(dna_sequence_return)
#the code works, yay!