# Triangle area finder based on the vertices coordinates

a = input('Enter the coordinates of the vertice A separated by space: ')
b = input('Enter the coordinates of the vertice B separated by space: ')
c = input('Enter the coordinates of the vertice C separated by space: ')

a = a.split()
b = b.split()
c = c.split()

a = [int(x) for x in a]
b = [int(x) for x in b]
c = [int(x) for x in c]

print(f'\nThe are of the given triangle is: {abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) * 0.5}')
