a = int(input('Put first digit: '))
b = int(input('Put second digit: '))
operation = input('Put operation +, -, *, /: ')

if operation == '+':
    print(a + b)

elif operation == '-':
    print(a - b)

elif operation == '*':
    print(a * b)

elif operation == '/':
    if b == 0:
        print('Error: You cannot divide by zero')
    else:
        print(a / b)

else:
    print('Invalid operation')

