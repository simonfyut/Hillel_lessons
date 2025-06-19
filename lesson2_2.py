number = int(input("Enter numbers: "))

number1 = number % 10
number2 = (number // 10) % 10
number3 = (number // 100) % 10
number4 = (number // 1000) % 10
number5 = (number // 10000) % 10
reversed_number = (number1 * 10000) + (number2 * 1000) + (number3 * 100) + (number4 * 10) + number5
print("Reversed number:", reversed_number)
