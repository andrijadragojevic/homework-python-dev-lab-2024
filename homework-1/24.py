# Variable switching

x = input("Enter the value of the first variable: ")
y = input("Enter the value of the second variable: ")

t = x  # temporary variable
x = y
y = t

print(f"\nThe value of the first variable is now: {x}")
print(f"The value of the second variable is now: {y}")