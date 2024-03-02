# Secret door code 

number_str = input("Enter a three-digit number: ")

number_str = number_str.replace(" ", "")
number_str = number_str.replace("-", "")

number = int(number_str)
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

digit_sum = first_digit + second_digit + third_digit
digit_product = first_digit * second_digit * third_digit

print(f'The secrect code is: {digit_product-digit_sum}')

