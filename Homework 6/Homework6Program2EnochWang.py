# Enoch Wang
# 3/4/2020
# Homework 6 Program 2
# CSCI 6651
# Professor Gulnora Nurmatova 

import json
import os, os.path
import pathlib

if __name__ == '__main__': 
    
    quotes = []
    authors = []
    
    with open("quotes.json", 'r') as quotes_file:
    	data = json.load(quotes_file)
    	for node in data:
            quotes.append(node["text"])
            authors.append(node["author"])
            
    os.mkdir("Authors")
    os.chdir("Authors")
    cwd = os.getcwd()
    for i in range(0, len(authors)):
        os.chdir(cwd)
        directory = str(authors[i])
        if (not os.path.exists(directory)):
            os.mkdir(directory)
            os.chdir(directory)
            print("Created ", directory)
            out = open("quote_1.txt", "w")
            out.write(quotes[i])
            out.close()
        elif(os.path.exists(directory)):
            os.chdir(directory)
            file_count = 0
            for path in pathlib.Path(".").iterdir():
                if path.is_file():
                    file_count = file_count + 1
            file_count = file_count + 1
            out = open("quote_" + str(file_count) + ".txt", "w")            
            out.write(quotes[i])
            out.close()
        else:
            print("Directory Exists")
        