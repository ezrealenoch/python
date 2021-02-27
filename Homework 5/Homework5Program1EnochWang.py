# Enoch Wang
# 2/26/2020
# Homework 5 Program 1
# CSCI 6651
# Professor Gulnora Nurmatova 

def my_range(*params):
    i = 0
    if (len(params) == 1):
        while i < params[0]:
            yield i
            i = i + 1
    elif (len(params) == 2):
        i = params[0]
        while i < params[1]:
            yield i
            i = i + 1
    elif (len(params) == 3):
        i = params[0]
        while i < params[1]:
            yield i
            i = i + params[2]
        
    
    
if __name__ == '__main__': 
    for i in my_range(0,5):
       print(i)
    
    for i in my_range(0,5,2):
        print(i)