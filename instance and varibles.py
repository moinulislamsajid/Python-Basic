'''class student():
    def stu(name,roll):
        name = 'sajid'
        roll = '20'
        print(name,roll)




value = student()
value.stu(20)
'''



class Employee:
    no_of_student = 10 #this is class varibale it is almost fixed because this is class a varibale can not be overright if any change to need the chnage the class varible than change the object variblem 
    pass

sajid = Employee()
sakib = Employee()

sajid.name='Moinul islam sajid'
sajid.age = 20
sajid.roll = 19

sakib.name='Moinul islam sajid'
sakib.age = 20
sakib.roll = 19
sakib.no_of_student = 15

"""print(sajid.no_of_student)
print(sakib.no_of_student)"""
#print(sajid.__dict__)
print(sakib.__dict__)








