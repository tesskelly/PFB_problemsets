#!/usr/bin/env python3
#!/usr/bin/env python3
#3. Modify your function so that it takes two arguments, the DNA string and the max length of each line.
dna_string = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'


# def dna_sequence(dna,width=80):
#     dna = dna.replace("\n",'')
#     seq_list = [] 
#     for i in range(0, len(dna), width):
#         sub_dna = dna [i:i+width] 
#         seq_list.append(sub_dna)
#     dna_sequence = '\n'.join(seq_list)
#     return dna_sequence

# dna_sequence_return = dna_sequence(dna_string)
# print(dna_sequence_return)

# Need to define width, or else you will get an error. Changing width to 10 would give you the sequence in incriments of 10 stacked on top of each other. 

def dna_sequence(dna,width):
    dna = dna.replace("\n",'')
    seq_list = [] 
    for i in range(0, len(dna), width):
        sub_dna = dna [i:i+width] 
        seq_list.append(sub_dna)
    dna_sequence = '\n'.join(seq_list)
    return dna_sequence

# dna_sequence_return = dna_sequence(dna_string,widthhh=80)
widthhh=80
# dna_sequence_return = dna_sequence(dna_string,widthhh)
dna_sequence_return = dna_sequence(width = widthhh, dna = dna_string)
#dna_sequence_return = dna_sequence(dna_string,80)
print(dna_sequence_return)

# Need to define width, or else you will get an error. Changing width to 10 would give you the sequence in incriments of 10 stacked on top of each other. 
# the code works, I think