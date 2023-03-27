'''one = int(input())
print("type one or two")
two = int(input())
new = bool(two)
if new == True:
    for i in range(1,one+1):
        print("*",end="")
    print()
elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

'''

print("Patttarn print")
one = int(input("Enter num how many numuber you wanted : "))
print("Enter 0 or 1 ")
bool_value = input("Enter 1 for true 0 for false")

if bool_value == "1":
    for i in range(0,one+1):
        print("*"*int(i))

if bool_value == "0":
    for i in range(one,0,-1):
        print("*"*int(i))



