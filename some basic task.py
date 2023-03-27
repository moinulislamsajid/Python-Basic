#function and docstring

"""class name:
    def __init__(self):
            name = 'sajid'
            age = 20

    def function(x,y):
      avarge = (x+y) /2
      print(avarge)
look = name()
name.function(10,20)

"""
"""def look(c,d):
    res = c+d
    return res

fol = look(10,20)
print(fol)"""






'''def din(h,b,g):
    math = h * b * g
    return math

vol = din(10,20,40)
print(vol)'''


from unittest import result


def sum(x,y):
    """ this function has two argument cannot sum 3 argument"""
    result = x+y
    print(result)


sum(10,20)
print(sum.__doc__)
