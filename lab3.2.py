def sum_of_digits(number):
    total_sum = 0
    number = abs(number)   
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10    
    return total_sum
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits is: {result}")
