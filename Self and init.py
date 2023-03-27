class student:
   no_of_student = 10
   def local(self):
    return (f"Name is {self.name}. Roll is {self.roll} Salary is {self.salary}")



sajid = student()
sakib = student()


sajid.name = 'Moinul islam sajid'
sajid.roll = 20
sajid.salary = 200000


sakib.name = 'Samiur Rohman Sakib'
sakib.roll = 10
sakib.salary = 10000000

print(sajid.printdetails())
