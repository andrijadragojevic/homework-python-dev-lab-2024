time = int(input("Enter the time (only hours): "))

print("You can't work, it's too noisy!!") \
if time < 6 or time in range(13, 17) or time >= 22 \
else print("You can work!")