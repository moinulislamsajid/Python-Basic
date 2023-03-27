from re import X
from this import d


l = 10  
def globals():
    global l
    print("this is global keywod")


globals()
print(l)    #when use to global varibale and local varible than print korla sob somay global varibale print korba
            # scope means value all time eqal thakba i mean global varible soman thakba  than function ar modda soman thakba print o soman korba that it

def sajid():
    x = 20
    def durjoy():
        global x
    print("Ayman Sajid")
    durjoy()
    print(x)

sajid()
