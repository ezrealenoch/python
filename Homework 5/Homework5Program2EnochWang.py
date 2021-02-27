# Enoch Wang
# 2/26/2020
# Homework 5 Program 2
# CSCI 6651
# Professor Gulnora Nurmatova 


def bunnyEars2(bun):
    if (bun % 2) != 0:
        return 2 + bunnyEars2(bun-1)
    else:
        if bun == 0:
            return 0
        return 3 + bunnyEars2(bun-1)
    
    
if __name__ == '__main__': 
    print(bunnyEars2(0))
    print(bunnyEars2(1))
    print(bunnyEars2(2))
    print(bunnyEars2(3))
    print(bunnyEars2(4))