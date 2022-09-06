import sys
class Sales:
    def __init__(self):
        self.L = []
        self.ReadData()
    def PrintMinue(self):
        print("""
        1- Print All Sales
        2- Print Sales for D
        3- Print Sum of sales for D
        4- Print Sum of sales for Product
        0- End
        """)
    def PrintAllSales(self):
        for i in self.L:
            print(i)
    def PrintSalesforD(self,D):
        for i in self.L:
            if i[3]==D:
                print(i)
    def PrintSumofsalesforD(self,D):
        Sum = 0
        for Product,Price,Qty,Day in self.L:
            if Day==D:
                Sum+=(Price*Qty)
        print(Sum)
    def PrintSumofsalesforProduct(self,P):
        Sum = 0
        for Product,Price,Qty,Day in self.L:
            if Product==P:
                Sum+=(Price*Qty)
        print(Sum)
    def Run(self):
        while True:
            self.PrintMinue()
            Choice = int(input())
            if Choice == 1:
                self.PrintAllSales()
            elif Choice == 2:
                D = input("Pick value for Day: ")
                self.PrintSalesforD(D)
            elif Choice == 3:
                D = input("Pick value for Day: ")
                self.PrintSumofsalesforD(D)
            elif Choice == 4:
                P = input("Pick value for Product: ")
                P = P.lower()
                self.PrintSumofsalesforProduct(P)
            elif Choice == 0:
                sys.exit()
    def ReadData(self):
        File = open("product.txt","r")
        for Line in File:
            l = Line.split()
            l[1] = float(l[1])
            l[2] = float(l[2])
            self.L.append(l)

Products = Sales().Run()

