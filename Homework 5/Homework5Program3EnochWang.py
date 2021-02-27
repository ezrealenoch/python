# Enoch Wang
# 2/26/2020
# Homework 5 Program 3
# CSCI 6651
# Professor Gulnora Nurmatova 

import time

def test():
    print("Doherty Threshold")
    time.sleep(0.4)
    return("Doherty Threshold Response")
    
def execution_time(r):
    def inner():
        start = time.time()
        s = r()
        end = time.time()
        total = end - start
        return  {"This function took ":total, "seconds to execute and returned":s}
    return inner

    
if __name__ == '__main__': 
   dec = execution_time(test)
   res = dec()
   print(res)