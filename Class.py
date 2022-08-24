from asyncio.windows_events import NULL


class Computer:
    def __init__(self,a):
        self.RAM = 12
        self.color = "Black"
        self.a = a
    def printData(self):
        print(self.a)
        print("RAM=",self.RAM)
        print("color=",self.color)


x = Computer(5)
#x.printData()
#x.RAM = 6
#x.printData()
Name = "Ali"
print(type(Name))
print(type(x))
print(dir(Name))
print(dir(x))