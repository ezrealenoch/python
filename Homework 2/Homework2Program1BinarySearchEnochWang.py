# Enoch Wang
# 2/5/2020
# Homework 2 Program 1
# CSCI 6651
# Professor Gulnora Nurmatova 

# Binary Search Algorithing that takes in a min, max, and number of recursive iterations
def BinarySearch(low, high, tries):     
    if low == 99:
        tries +=1
        userinput = input("Is it 100? (yes/no)")
        s1 ="Yeey! I got it in "
        s2 = str(tries)
        s3 = "!"
        print(s1 + s2 + s3)
        return mid
    elif high == 1:
        tries +=1
        userinput = input("Is it 1? (yes/no)")
        s1 ="Yeey! I got it in "
        s2 = str(tries)
        s3 = "!"
        print(s1 + s2 + s3)
        return mid
    elif high >= low:
        tries += 1
        mid = (high + low) // 2
        s1 = "Is it " 
        s2 = str(mid)
        s3 = "? (yes/no)"
        userinput = input(s1 + s2 + s3)
        if userinput == "yes":
            s1 ="Yeey! I got it in "
            s2 = str(tries)
            s3 = "!"
            print(s1 + s2 + s3)
            return mid
        elif userinput == "no":
            s1 = "Is it larger than "
            s2 = str(mid)
            s3 = "? (yes/no)"
            userinput = input(s1 + s2 + s3)
            if userinput == "yes":
                return BinarySearch(mid + 1, high, tries)
            elif userinput == "no":
                return BinarySearch(low, mid - 1, tries)
            else:
                return -1
        else:
            return -1
    else:
        return -1
    

if __name__ == '__main__':   
    # Base console output
    userinput = input("Hi, what is your Name? ")
    print("Hello " + userinput + "! Let's play a game!")
    print("Think of a random number from 1 to 100, and I'll try to guess it!")
    
    # While loop to play the game multiple times
    i = 1
    while i == 1:
        result = BinarySearch(1,100,0)
        if result == -1:
            print("Error")
        userinput = input("Do you want to play more?")
        if userinput == "no":
            print("Bye-bye")
            i = 0
        elif userinput == "yes":
            i = 1
        else:
            print("Error Incorrect Input")
            i = 0

            
                

    
