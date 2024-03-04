# Round table tape calculator

from math import pi, sqrt


table_area = float(input("Enter the area of the table [m^2]: "))

table_circumference = 2 * pi * sqrt(table_area / pi)

print(f'The table circumference is {table_circumference}m')