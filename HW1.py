'''
n = 8
for i in range(1,n+1):
    if i%2==0:
        print('$'*i)
    else:
        print('*'*i)
'''

n = 8
for i in range(1,n+1):
    if i%2==0:
        for j in range(i):
            print('$',end='')
    else:
        for j in range(i):
            print('*',end='')
    print()

n = 8
for i in range(1,n+1):
    for j in range(i):
        if i%2==0:
            print('$',end='')
        else:
            print('*',end='')
    print()
