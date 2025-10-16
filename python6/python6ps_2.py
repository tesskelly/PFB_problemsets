#!/usr/bin/env python3
with open("Python_06.txt","r") as poem_python06_read, open ("Python_06_uc.txt","w") as Python_06_uc:
    for line in poem_python06_read:
        line = line.rstrip()
        line = line.upper()
        print(line)

#the code works yay!