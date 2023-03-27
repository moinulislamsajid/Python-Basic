# problem if any list you have your input is five if five greaer than tohla sob five ar oprar gula print hoba
#list_2 = [1,2,3,4,5,6,7,8,9]
'''if range(len(list_2)) > 5:
    print(list_2)
'''
'''def greaterthan(num):
    return num > 5

local = list(filter(greaterthan,list_2))  # when we do not called list when printed object value
print(local)'''


# give an list 1 to 20 you have printed to only any 7 value

list_1 = [1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def function(num):
   return num > 13

val = list(filter(function,list_1))
print(val)
