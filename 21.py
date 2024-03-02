# Safe code

number_str = input("Enter a four-digit number: ")

number_str = number_str.replace(" ", "")
number_str = number_str.replace("-", "")

number = int(number_str)

first_digit = number // 1000
second_digit = (number // 100) % 10
third_digit = (number // 10) % 10
fourth_digit = number % 10

print(f'The secred safe code is: {((first_digit + fourth_digit)**2 - (second_digit**2 - third_digit**2))}')
