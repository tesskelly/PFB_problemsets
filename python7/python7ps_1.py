#!/usr/bin/env python3
# 1. In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position.
import re
with open("python_07_nobody.txt","r") as python_07_nobody: #python can't get the contents of a file until you tell it to fead the file. Store as a variable for less typing? also think this is just the way you do it. 
    for line in python_07_nobody: #for each line (you could type pencil or something and python knows that it still means line.) in python07_nobody
        for found in re.finditer(r'Nobody',line):
            print(found.start(0))

#the code works!!

#or do this 
import re
with open("python_07_nobody.txt","r") as python_07_nobody: #python can't get the contents of a file until you tell it to fead the file. Store as a variable for less typing? also think this is just the way you do it. 
    contents = python_07_nobody.read()
    for found in re.finditer(r'Nobody',contents):
        print(found.end(0))

#this technically works, but it makes more sense to go line by line. Readout is 0, 28, 45...so on and so forth. Nobody 1 starts at position zero. Nodody 2 starts at position 28 in the file. Confusing to figure out where position 28 is. 
#remeber to toggle 1 version if you want to run the other. 