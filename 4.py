# Running distance calculator

print("\n Enter the following information down below\n")

stadium_length = float(input("Enter the length of the stadium [m]: "))
stadium_witdh = float(input("Enter the witdh of the stadium [m]: "))

stadium_circumference = (2 * stadium_length) + (2 * stadium_witdh)

laps = float(input("Enter the number of laps: "))

print(f'\nSportist has ran the distance of:\n{stadium_circumference*laps} meters')