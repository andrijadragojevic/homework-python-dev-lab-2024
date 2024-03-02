# Quadratic equation solver

print("\nEnter the values of the equaton in the following format [ax^2 + bx + c = 0] by entering a, b and c values respectively in the next few lines\n\n")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = (b**2) - (4*a*c)
if discriminant > 0:
    print("\n\nThe equation has two real roots\n")
    root_one = (-b + (discriminant**0.5))/(2*a)
    root_two = (-b - (discriminant**0.5))/(2*a)
    print("\nThe roots are:\n\n" + str(root_one) + "\n" + str(root_two))
  
elif discriminant == 0:
    print("\n\nThe equation has one real root\n")
    root_one = (-b + (discriminant**0.5))/(2*a)
    print("\nThe root is " + str(root_one))
  
else:
    print("\nThe equation has no real roots")

print("\n")