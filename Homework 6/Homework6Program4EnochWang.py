# Enoch Wang
# 3/4/2020
# Homework 6 Program 4
# CSCI 6651
# Professor Gulnora Nurmatova 

import os, os.path
from os import path
from os import walk

def search(filepath, filename):
    os.chdir(filepath)
    f = []
    for (dirpath, dirnames, filenames) in walk(filepath):
        f.extend(filenames)
        break
    for i in range(0, len(filenames)):
        if(filename == filenames[i]):
            return filepath + "\\" + str(filename)
    for i in range(0, len(dirnames)):
        potato = search((filepath + "\\" + dirnames[i]),filename)
        if potato is not None:
            return potato
        os.chdir(filepath)
        
           
if __name__ == '__main__': 
    filepath = input("Enter a Path: ")
    filename = input("Enter a Filename: ")
    
    if (path.exists(filepath)):
        print(search(filepath, filename))
        
    else:
        print("Path not found")
        
    