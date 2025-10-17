#!/usr/bin/env python3
#In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).
import re
with open("python_07_nobody.txt","r") as python_07_nobody_read, open("Tess.txt","w") as Tess: #python can't get the contents of a file until you tell it to fead the file. Store as a variable for less typing? also think this is just the way you do it. 
    for line in python_07_nobody_read: #for each line (you could type pencil or something and python knows that it still means line.) in python07_nobody
        Tess = re.sub(r'Nobody',r'Tess', line)
        print(Tess)

#for found in re.sub(r'Nobody',r'Tess', line):
#don't do this because it interprets this as a string and looping over. string goes letter by letterimport re
with open("python_07_nobody.txt","r") as python_07_nobody_read, open("Tess.txt","w") as Tess: #python can't get the contents of a file until you tell it to fead the file. Store as a variable for less typing? also think this is just the way you do it. 
    for line in python_07_nobody_read: #for each line (you could type pencil or something and python knows that it still means line.) in python07_nobody
        Tess = re.sub(r'Nobody',r'Tess', line)
        print(Tess)

