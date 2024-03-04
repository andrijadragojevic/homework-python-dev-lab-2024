# Apartment evaluation

apartment_size = int(input("Enter the size of the apartment in m2: "))
apartment_parking = int(input("If the apartment has a parking space, enter 1, otherwise enter 0: "))
apartment_location = int(input("If the apartment is located in the city, enter 3, if it's on the outskirts of the city enter 2, if it's outside of the city enter 1: "))

price_per_square = 1200
participation_fee = 1000

size_price = apartment_size * price_per_square
location_price = 5 * size_price * apartment_location
parking_price = 10 * location_price * apartment_parking

print(f'\nThe price of the apartment is: {size_price + location_price + parking_price + participation_fee} euros')