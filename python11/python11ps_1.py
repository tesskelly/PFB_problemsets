#!/usr/bin/env python3
# Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function.
class DNARecord(object):
    def __init__(self,sequence,gene_name,species_name):
        # sequence = 'ACGTAGCTGACATC'
        # gene_name = 'ABC1'
        # species_name = "Drosophilia melanogaster"
        self.sequence = sequence.upper()
        self.gene_name = gene_name
        self.species_name = species_name
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count)/length 
        return at_content 
    def get_sequence_length(self):
        return len(self.sequence)
# create a new DNArecord object with user defined data
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT','ABC1', 'Drosophila melanogaster')
dna_rec_obj_2 = DNARecord('ATATATTATTATATTATA','COX1','Homo sapiens')

for d in [dna_rec_obj_1, dna_rec_obj_2]:
    print('name:' ,d.gene_name,' ','seq:',d.sequence ,"sequence length:", d.get_sequence_length(), "species name:", d.species_name, "AT_content:" , f"{d.get_AT() * 100:.2f}%")
#the code works, thank you chat GPT!