# Area and curcimference of a rectangle calculator

side_a = float(input( "Enter the length of side a [cm]: "))
side_b = float(input( "Enter the length of side b [cm]: "))

rect_curcimference = (2 * side_a) + (2 * side_b)
rect_area = side_a * side_b

print( "The curcimference of the rectangle is " + str(rect_curcimference) + "cm")
print( "The area of the rectangle is " + str(rect_area) + "cm2")