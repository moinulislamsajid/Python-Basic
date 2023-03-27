class Dad:
    fothball = 5

class Son(Dad):
    singer = 10
    def local_singer(self):
        return (f"He sing a song {self.singer} times")

class Grandson(Son):
   singer = 3
   def local_singer(self):
        return (f"He sing a song {self.singer} times")   # this is a method or function overloading


sajid = Grandson()
val = sajid.local_singer()
print(val)