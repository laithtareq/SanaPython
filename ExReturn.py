#A = 5*x + 4*y

#B = A*10

def Calculate_A(x,y):
    A = 5*x + 4*y
    #print(A)
    return A

def Calculate_B(A):
    B = A*10
    #print(B)
    return B

Q = Calculate_A(5,6)
B = Calculate_B(Q)

print(Q)
print(B)

