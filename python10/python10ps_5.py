#!/usr/bin/env python3
#5. Create a new function that calculates the GC content of a DNA sequence. 
    # it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
    # example percentGC = gc_content('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA') or percentGC = gc_content(dna)
dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
c_count = dna.count('C')
g_count = dna.count ('G')
dna_len = len(dna)
gc_content = (c_count + g_count)/dna_len
print(gc_content)


def gc_content(dna): #give the function a name and parameter 'dna'
    c_count = dna.count ('C')
    g_count = dna.count ('G')
    dna_len = len(dna)
    gc_content = (c_count + g_count)/len(dna)
    return gc_content #return the value to the code that called this function

dna_gc = gc_content(dna)
print(f'This sequence is {dna_gc:.2%} GC')


# the code works kms