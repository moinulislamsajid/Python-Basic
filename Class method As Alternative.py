class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    @staticmethod  #this is called decoroted
    def printgood(string):
        print("This is a goodthing"+string)
        return "this is Dhaka"

stu1 = student("Ayman Sajid",20)
print(stu1.printgood("Ayman sajid"))