
number_input = int(input("Enter a numbers: "))
number1 = number_input // 1000
number2 = (number_input % 1000) // 100
number3 = (number_input % 100) // 10
number4 = number_input % 10

print(number1)
print(number2)
print(number3)
print(number4)
