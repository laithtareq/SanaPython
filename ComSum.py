sum = 0
n = 5
for i in range(1,n+1):
    sum+=i
    for j in range(1,i+1):
        print(j,end='')
    if i%2==0:
        print('$',end='')
    else:
        print('*',end='')
    print(sum)