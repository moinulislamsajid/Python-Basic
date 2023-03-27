'''from math import sqrt
num = [2,3,4,5,6,7,8,9]
look = list(map(sqrt, num))
print(look)
'''

'''from unittest import result


roll = [3,4,5,6,7,8]
result = list(map(lambda x: x*x, roll))
print(result)


fall = [9,8,7,6,5,4,3,2]
lol = list(map(lambda x : x*x*x,fall))
print(lol)
'''
'''def square(a):
    return a*a

def cube(a):
    return a*a*a

func = (square,cube)
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)'''

# problem you have /no input/ so you find output every value are /squire/ and /cube/ value to /return/ 1 to 10 list eah other value are printed /list[0 0]/
import re


def squire(a):
    return a*a
def cube(a):
    return a*a*a
fun = (squire,cube)
for i in range(11):
    val = list(map(lambda x:x(i),fun))
    print(val)


list = [2,3,4,5]
res = list(map(lambda x: x*2,list))
print(res)


