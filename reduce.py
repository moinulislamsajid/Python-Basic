from array import array
from functools import reduce
from traceback import print_tb
"""from functools import reduce
array = int(input("Enter an array : "))
sum = 0
for i in array:
    sum+=i

print(sum)"""
## GIVEN AN ARRAY SUM 

'''list = [34,23,54,65,76,87,34,23,45]

sum = 0
for i in list:
    sum = sum + i
 
print(sum)
'''
'''lol = [43,55,34,21,45,67,78,54,32]
sm = 0
for i in lol:
    sm = sm+i
print(sm)
'''
'''list = [23,32,43,54,65,32,43,12,12]
num = reduce(lambda x,y:x+y, list)
print(num)'''

lol = [23,12,12,12,12,12]
fol = reduce(lambda a,b:a+b,lol) 
print(fol)
