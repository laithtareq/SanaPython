class Ticket:
    count = 0
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
        self.price = 0
        Ticket.count+=1
        self.assignPrice()
    def assignPrice(self):
        Tax = 0.02
        if self.age>25:
            self.price = 200+200*Tax
        elif self.age>=6 and self.age<=25:
            self.price = 125+125*Tax
        elif self.age<6:
            self.price = 0
    def printReport(self):
        Data = """
        id    : {}
        Name  : {}
        Age   : {}
        Price : {}""".format(self.id,self.name,self.age,self.price)
        print(Data)

id1 = 1234
name1 = "Ali"
age1 = 30
Father = Ticket(id1,name1,age1)
Mother = Ticket(1235,"Rana",24)

Father.printReport()
Mother.printReport()
    
        
