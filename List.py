'''
x = [1,4,5,8,9,7]
print(x[1:4])
print(x[1:])
print(x[:4])
print(x[1:10:3])
'''

'''
a = 10
b = a
print(b)
a = 7
print(b)

x = [1,4,5,1,8,9,7]
y = x.copy()

print(y)
x[1] = 5
print(y)
print(x)
print(type(x))
print(x.index(1))
print(dir(x))
x.insert(3,40)
print(x)
del x[0]
print(x)'''
x = [1,4,5]
y = [7,5,9]
print(x+y)
print(x*3)


Name = 'Layth'
print(Name[0])
#Name[0] = 'O'

print(len(x))
print('Done')
Name = 'Ali'
Mark = "B"
print(Name,'Your Grade is',Mark)
print('{0} Your Grade is {1}, Good work {0}'.format(Name,Mark))
