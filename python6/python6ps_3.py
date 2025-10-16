#!/usr/bin/env python3
#Open and print the reverse complement of each sequence in Python_06.seq.txt. 
#Each line is the following format: seqName\tsequence\n. 
#Make sure to print the output in FASTA format including the sequence name and a note in the description that this is the reverse complement. 
#Print to STDOUT and capture the output into a file with a command line redirect '>'.

with open("Python_06.seq.txt","r") as Python_seq_file:
    for line in Python_seq_file:
        line = line.rstrip() #need to strip the white space because the new line characters do not have base characters. Makes it harder for the program to deal with. 
        line = line.split()
        print(line)
        line[1]= line[1].replace('A','t').replace('T','a').replace('C','g').replace('G','c')
        print(line)
        line[1]= line[1][::-1]
        print(line[1])
        break

#the code works yayyyy!!!
        

        