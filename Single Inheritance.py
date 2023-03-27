class Bangladesh:
    def __init__(self,capital,liberation,district):
        self.capital = capital
        self.liberation = liberation
        self.district = district
    def print_local(self):
        print(f"This Capital is {self.capital} Won liberation war {self.liberation} And their district {self.district} ")

class Dhaka(Bangladesh):
   def hey_dho(slef):
    print("Bangladesh is a wonderful country it has many historical place it has large amout of people")

cap = Dhaka("Dhaka",1971,64)
Dhaka.print_local(cap)
Dhaka.hey_dho(cap)



    
