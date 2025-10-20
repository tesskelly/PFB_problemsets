#!/usr/bin/env python3
#5. Create a new function that calculates the GC content of a DNA sequence. 
    # it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
    # example percentGC = gc_content('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA') or percentGC = gc_content(dna)

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
dna = dna.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
print(dna[::-1])


def rev_comp (dna): #give the function a name and parameter 'dna'
    dna = dna.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    dna_rev_comp = (dna[::-1])
    return dna_rev_comp #return the value to the code that called this function

dna_reverse_compliment = rev_comp(dna)
print (f'The reverse compliment sequence is {dna_reverse_compliment}')

#the code works. The correct answer is "The reverse compliment sequence is tccagggaagcgtgtcaccgtcgtggaaagcacg".