def FindMark(grade):
    #grade = 90
    if grade > 85:
        print("A")
    
    elif grade > 75:
        print("B")
    
    else:
        print("F")

#FindMark(90)
#FindMark(80)
#FindMark(60)

def Sum(x=0,y=0):
    z = x+y
    #print(x+y)
    return z

print(Sum(5,10))
Sum(5)
Total = Sum(4,5)
print(Total)

