'''class Phone:
    def samsung(self):
        print("A51")

    def iphone(self):
        print("i !5")

class local(Phone):
    def hey(self):
        print("Wlaton")

ban = local()
ban.samsung()
ban.iphone()
ban.hey()'''

class laptop:
    def __init__(self):
        self.model = 'hp'
        self.price = 500000

    def local(self):
        print("Bangladesh")

ban = laptop()
ban.local()      