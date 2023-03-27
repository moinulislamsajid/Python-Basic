class Dhaka:
    def __init__(self,district,upzilla,proshova):
        self.district = district
        self.upzilla = upzilla
        self.proshova = proshova

    def total_dh(self):
        print(f"Total District {self.district} And Upzilla {self.upzilla} Proshova {self.proshova}")


class Faridpur:
    def __init__(self,estsblishname,totalpeople):
        self.estsblishname = estsblishname
        self.totalpeople = totalpeople
    def printdeatails(self):
       return (f"Faridpur Establish name {self.estsblishname} And total people {self.totalpeople}")

class Faridpur_sador:
    pass
local = Faridpur("Faridshah",292999292929)
otahal = local.printdeatails()
print(otahal)      # jokon return value print korbo tokon variable name = objectname.function/methodname

        