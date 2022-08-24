class ticket:
    #c = 0
    def __init__(self,CustName,Age,HotelStar,Duration):
        self.Age = Age
        self.HotelStar = HotelStar
        self.Duration = Duration
        self.CustName = CustName
        #ticket.c+=1
    def ComputeExpenses(self):
        # Calculate The Starting Price depend on the age
        if self.Age>12:
            price = 45
        else:
            price = 25
        # Add The Hotale star Price
        if self.HotelStar==3:
            price += self.Duration*10
        elif self.HotelStar==4:
            price += self.Duration*15
        elif self.HotelStar==5:
            price += self.Duration*20
        # Add 16% Tax to the total price
        price*=1.16
        #price+=price*0.16
        # Return the total price
        return price
    def PrintReport(self):
        TotalPrice = self.ComputeExpenses()
        Data = """
        Custmer Name: {}
        Age         : {}
        Hotal Star  : {}
        Duration    : {}
        Total Price : {}""".format(self.CustName,self.Age,self.HotelStar,self.Duration,TotalPrice)
        print(Data)


CustName = input("Enter The Custmer Name: ")
Age = int(input("Enter The Custmer Age: "))
HotelStar = int(input("Enter The Hotal Star: "))
Duration = int(input("Enter The Duration: "))
MyTicket = ticket(CustName,Age,HotelStar,Duration)
MyTicket.PrintReport()
