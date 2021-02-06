# Enoch Wang
# 2/5/2020
# Homework 2 Program 2
# CSCI 6651
# Professor Gulnora Nurmatova 


# Shuffles the string in the order given by the indices
def ShuffleString(s, indices):
    l = list(s)
    string = ""
    x = 0
    for j in range(0,len(indices)):
        for i in range(0,len(indices)): 
            if x == indices[i]:
                string = string + string.join(l[i])
                x = x + 1
                break
    return string

        

if __name__ == '__main__': 
    
    # set string s =
    s = "codeleet"
    
    # set indices =
    indices = [4,5,6,7,0,2,1,3]
    
    # Print Output
    print(ShuffleString(s,indices))
    