##use constructor
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdeatils(self):
        print(self.name,self.age)


##input
h1=Human('Mantu Raj',20)
h1.printdeatils()

print(type(Human))


        