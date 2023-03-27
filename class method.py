from this import d
from unicodedata import name


class student:
    no_of_student = 50
    def __init__(self,name,salary,id):
        self.name = name
        self.salary = salary
        self.id = id
'''
    @classmethod
    def change_student(cls):
       # cls.no_of_student =  newleaves
'''



stu1 = student("Sajid",20000,323)
stu2 = student("Skaib",1000,101)
stu1.change_student(70)

print(stu1.no_of_student)





    