# Digit sum of the three-digit number

number_str = input("Enter a three-digit number: ")

number_str = number_str.replace(" ", "")
number_str = number_str.replace("-", "")

number = int(number_str)
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

print(f'\nThe sum of the digits of the given number is {first_digit + second_digit + third_digit}')

