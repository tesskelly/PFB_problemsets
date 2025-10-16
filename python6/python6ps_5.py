#!/usr/bin/env python3
#FASTQ File Parsing: 
#A FASTQ file has 4 lines per sequence record:
# 1. Begins with a '@' character and is followed by a sequence identifier and an optional description (like a FASTA title line).
# 2. The raw sequence letters
# 3. Begins with a '+' character and is optionally followed by the same sequence identifier (and any description) again.
# 4. The quality values for each sequence character. This line is required to contain the same number of symbols as letters in the sequence.
# A FASTQ file containing a single sequence will have a format like this:
# @SEQ_ID  
# GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT  
# +  
# !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65  
# The quality scores are denoded with ASCII characters. 
# The byte representing quality runs from 0x21 (lowest quality; '!' in ASCII) to 0x7e (highest quality; '~' in ASCII).
# Here are the quality value characters in left-to-right increasing order of quality (ASCII):
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~

# For this problem open the FASTQ file Python_06.fastq and read each line to calculate and report:
# total number of lines
# total number of sequence IDs 
# total number of characters
# total number of nucleotides
# average line length of all the lines
# average line length of the lines that contain sequences

# Goal of this problem: generate a couple of gene list that are saved in files, add their contents to sets, and compare them.

#Generate gene lists: ...don't feel like typing this. refer to problem set. 

#this is too hard. don't feel like doing this right now. 




