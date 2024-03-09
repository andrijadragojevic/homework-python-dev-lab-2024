a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))

print("The lenghts you gave, make up a triangle") \
if a + b > c and a + c > b and b + c > a \
else print("The lenghts you gave, do not make up a triangle")