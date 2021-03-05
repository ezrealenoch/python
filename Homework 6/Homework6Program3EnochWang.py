# Enoch Wang
# 3/4/2020
# Homework 6 Program 3
# CSCI 6651
# Professor Gulnora Nurmatova 

import shelve
import time

def shelf():
    sh = shelve.open("my_items")
    sh["list"] = [1,2,3,4]
    sh
    sh["list"]
    return

def dictionary():
    dictionary = {
        "list": [1,2,3,4]
    }
    print(dictionary)
    
def execution_time(r):
    def inner():
        start = time.time()
        s = r()
        end = time.time()
        total = end - start
        return  {"This function took ":total, "seconds to execute and returned":s}
    return inner

    
if __name__ == '__main__': 
   dec = execution_time(shelf)
   res = dec()
   print("shelf time: " + str(res))
   
   dec = execution_time(dictionary)
   res = dec()
   print("dictionary time: " + str(res))
   