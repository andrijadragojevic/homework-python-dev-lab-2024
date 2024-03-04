# Quadratic trinomial

print("Enter the a,b,c from the mathematical expression in the following format:\na^2 + b^2 + c^2 + 2ab + 2bc + 2ac\n")

a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = float(input("Enter the c: "))

print(f"\nThe quadratic trinomial result is {a**2 + b**2 + c**2 + 2*a*b + 2*b*c + 2*a*c}")