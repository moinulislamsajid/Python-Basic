class A:
    local = "I am a class varibale in class A"
    def __init__(self):
        self.hey = "I am in class A"


class B:
    def __init__(self):
        self.hey = "I am in class A"
    loca2 = "I am in class B"
    pass



a = A()
b = B()
print(b.hey)
       
