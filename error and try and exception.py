print('Enter first num : ')
n1 = input()
print('Enter second num : ')
n2 = input()
try : 
    print('The answar is : ',int(n1)+int(n2))
except Exception as f:
    print("Str type and int type can not be sum")

a = 5
b = 2
try : 
  print(a/b)
  n = input("Enter : ")
  print(n)
except ZeroDivisionError as e:
    print("you cannot divison by zero")
except ValueError as e :
    print("invalid error")



