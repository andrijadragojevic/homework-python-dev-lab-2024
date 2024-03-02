# The avarage number of points

N = int(input("Enter the number of students: "))
K = int(input("Enter the number students of the second page: "))
p1 = float(input("Enter the avarage number of points of the first page: "))
p2 = float(input("Enter the avarage number of points of the second page: "))

first_page_points = (N-K) * p1
second_page_points = K * p2

avarage_points = (first_page_points + second_page_points) / N

print("\nThe avarage number of points is: ", avarage_points)