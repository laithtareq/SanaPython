def ComputeExpenses(Age,HotelStar,Duration):
    # Calculate The Starting Price depend on the age
    if Age>12:
        price = 45
    else:
        price = 25
    # Add The Hotale star Price
    if HotelStar==3:
        price += Duration*10
    elif HotelStar==4:
        price += Duration*15
    elif HotelStar==5:
        price += Duration*20
    # Add 16% Tax to the total price
    price*=1.16
    #price+=price*0.16
    # Return the total price
    return price
def PrintReport(CustName,Age,HotelStar,Duration,TotalPrice):
    Data = """
    Custmer Name: {}
    Age         : {}
    Hotal Star  : {}
    Duration    : {}
    Total Price : {}""".format(CustName,Age,HotelStar,Duration,TotalPrice)
    print(Data)

CustName = input("Enter The Custmer Name: ")
Age = int(input("Enter The Custmer Age: "))
HotelStar = int(input("Enter The Hotal Star: "))
Duration = int(input("Enter The Duration: "))
TotalPrice = ComputeExpenses(Age,HotelStar,Duration)
PrintReport(CustName,Age,HotelStar,Duration,TotalPrice)
