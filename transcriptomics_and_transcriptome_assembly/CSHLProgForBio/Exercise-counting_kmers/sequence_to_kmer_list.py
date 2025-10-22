#!/usr/bin/env python

import os, sys



## method: sequence_to_kmer_list(sequence, kmer_length)
##
##  Extracts all kmers of a specified length from a sequence
##
##  ie.  sequence: GATCGATCGATCGA
##   and given kmer_length = 4
##   would yield
##                 GATC
##                  ATCG
##                   TCGA
##                    .... and so forth
##                       
##  input parameters:
##
##  seuqence : nucleotide sequence (type: string)
##
##  returns kmer_list : list of kmer sequences.
##                    ie.  ["GATC", "ATCG", ...]
    
def sequence_to_kmer_list(sequence, kmer_length):

    kmers_list = list()
    count = 0 
    ## begin your code
    for i in range(0,len(sequence)-kmer_length+1): # maybe add +1
        kmer = sequence[i:i+kmer_length] 
        kmers_list.append(kmer)


            

# # previous problem (pt A)
# def seq_list_from_fastq_file(fastq_filename):

#     seq_list = list()
#     count = 0
#     ## begin your code
#     with open(fastq_filename,"r") as reads_fq:
#         for line in reads_fq:
#             line = line.rstrip()
#             count += 1
#             if (count+2)%4 == 0:
#                 seq_list.append(line)
    ## end your code

    return kmers_list



def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} sequence kmer_length\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    sequence = sys.argv[1]
    kmer_length = int(sys.argv[2])

    kmers  = sequence_to_kmer_list(sequence, kmer_length)

    print(kmers)

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
# the code works!!