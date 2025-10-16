#!/usr/bin/env python3
#python6ps_3_practice_sequence.txt contains AATTGGCC
with open("python6ps_3_practice_sequence.txt","r") as Python_seq_file:
    for line in Python_seq_file:
        line = line.rstrip() #need to strip the white space because the new line characters do not have base characters. Makes it harder for the program to deal with. 
        line = line.split()
        print(line)
        line[0]= line[0].replace('A','t').replace('T','a').replace('C','g').replace('G','c')
        print(line)
        line[0]= line[0][::-1]
        print(line[0])
        break

#the code works! correct answer: ggccaatt