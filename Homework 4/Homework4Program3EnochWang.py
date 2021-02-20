# Enoch Wang
# 2/19/2020
# Homework 4 Program 3
# CSCI 6651
# Professor Gulnora Nurmatova 

def two_sum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j]) == target:
                newlist = [int(i),int(j)]
                return newlist
        
    
if __name__ == '__main__': 
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums,target))
    
    