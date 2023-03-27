# no need to declar function name 

n = 23
n2 = 50 

print(n2  if n2>n else n)   
def sfirst(s):
    return s
s= [[34,75],[45,85],[6,5],[1,6]]
s.sort(key=sfirst)
print(s) 

def look(d):
    return d
d= [[33,34],[55,60],[70,60],[50,70]]
d.sort(key=look)
print(d)
