'''def fact(n):
    if n==1:
        return 1
    else:
        return n* fact(n-1)
        


    
n = int(input("Enter a number : "))
print(fact(n))
'''

import re


def lol(n):
    fac = 1
    for i in range(n):
        fac = fac  * (i+1)
    return fac
    

n = int(input("Enter a number : "))
print(lol(n))