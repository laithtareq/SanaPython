import time,timeit



Code1 = """
X = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
Y = [4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6]
L = len(X)
Z = []
for i in range(L):
    Z.append(X[i]+Y[i])
#print(Z)
"""
Code2 = """
X = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
Y = [4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6]
Sum = lambda x,y:x+y
Z = map(Sum,X,Y)
"""
Time1 = timeit.timeit(Code1)
Time2 = timeit.timeit(Code2)
print(Time1)
print(Time2)