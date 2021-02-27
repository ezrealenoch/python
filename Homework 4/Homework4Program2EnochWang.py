# Enoch Wang
# 2/19/2020
# Homework 4 Program 2
# CSCI 6651
# Professor Gulnora Nurmatova 

def count_frequency(mylist):
    newlist = []
    # iterable = []
    uniqueList = list(set(mylist))
    uniques = len(uniqueList)
    for i in range(0,uniques):
        count = 0
        for j in range(0,len(mylist)):
            if uniqueList[i] == mylist[j]:
                count = count + 1
        newlist.append(count)
        
    # Sorting by Frequency Work in Progress
    
    # if len(uniqueList) == len(newlist):
    #     min = sys.maxsize
    #     max = 0 
    #     for i in range(0,len(newlist)):
    #         pos = 0
    #         for j in range(0,len(newlist)):
    #             if min > newlist[j] and max < newlist[j]:
    #                 min = newlist[j]
    #                 pos = j
    #         iterable.append(pos)
    #         max = min
    
    dic = {uniqueList[i]: newlist[i] for i in range(len(uniqueList))}
    return dic
    
    
if __name__ == '__main__': 
    mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
    print(count_frequency(mylist))