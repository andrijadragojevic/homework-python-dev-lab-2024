# Students meeting in the middle

a = input("Enter the coordinates of the first student separated by space: ")
b = input("Enter the coordinates of the second student separated by space: ")

a = a.split()
b = b.split()

a = [int(x) for x in a]
b = [int(x) for x in b]

middle = [(a[0] + b[0])/2, (a[1] + b[1])/2]

print(f"\nThe coordinates of the meeting spot are:\nX: {middle[0]}\nY: {middle[1]}")
