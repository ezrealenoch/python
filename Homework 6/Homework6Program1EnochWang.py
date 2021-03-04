# Enoch Wang
# 3/4/2020
# Homework 6 Program 1
# CSCI 6651
# Professor Gulnora Nurmatova 

import sys
from os import path

if __name__ == '__main__': 
    output = sys.argv[1]
    sys.argv.pop(0) 
    for i in range(1,len(sys.argv)):
        output = output + " " + str(sys.argv[i])
        
    # output = output.join(sys.argv)
    # output = output.replace("\\\\", "\\")
    # print("cd " + output)
    
    print("cd " + output)
    print(str(path.exists(output)))
    