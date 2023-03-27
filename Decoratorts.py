'''def look():
    print("Alhamdullah")


cool = look
cool()

del look
cool()'''

from cgitb import small
import io
import re

'''
def cool(num):
    if num == 0:
        return print
    if num == 1:
        return sum


f = cool(1)
print(f)

'''
'''
def executor(func):
    print('Allah vorsha')


executor(print)
'''
# Decorators

'''def look (full):
    def good():
        print("Banglasesh")
        full()
        print("Dhaka")
    return good


def bye():
    print("Faridpur")


bye = look(bye)
bye()'''

def phone(ios):
    def samsung():
        print("World number 1 smart phone company Ltd")
        ios()
        print("Most made by taiwan")
    return samsung

@phone # Decortors
def iphone():
    print("Most Vlubale Phone in the wrold")

#iphone = phone(iphone)
iphone()



