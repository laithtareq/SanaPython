Names = ['A','B','C','D']
Votes = [0,0,0,0]
n = 10
for i in range(n):
    NewName = input("Enter Name: ")
    ID = Names.index(NewName)
    Votes[ID]+=1
    Po
Max = max(Votes)
ID = Votes.index(Max)
print(Names[ID])