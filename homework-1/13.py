# Treasure map

import math

# Coordinate of the tree G(x1, y2) in format tree_coordinates = (x1, y2)
tree_coordinates = input(
    "Enter the coordinates of the treasure separated by a space: ")
tree_coordinates = tree_coordinates.split()

house_coordinates = input(
    "Enter the coordinates of the house separated by a space: ")
house_coordinates = house_coordinates.split()

# Changing the coordinates from strings to numbers
tree_coordinates = [int(x) for x in tree_coordinates]
house_coordinates = [int(x) for x in house_coordinates]

treasure_coordinates = [house_coordinates[0] + 2, house_coordinates[1] - 3]

print(f'\nCoordinates of the treasure are:\nX: {treasure_coordinates[0]}\nY: {treasure_coordinates[1]}')

print(f'\nThe distance between the treasure and the tree is: {math.sqrt((treasure_coordinates[0]-tree_coordinates[0])**2 + (treasure_coordinates[1]-tree_coordinates[1])**2)}')

print(f'\nThe distance including a vistit to the old house is: {math.sqrt((tree_coordinates[0]-house_coordinates[0])**2 + (tree_coordinates[1]-house_coordinates[1])**2) + math.sqrt(2**2 + 3**2)}')