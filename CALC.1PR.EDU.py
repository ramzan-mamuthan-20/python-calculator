
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(a,b,operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)

    elif operator == '*':
        return multiply(a, b)

    elif operator == '/':
        if n2 == 0:
            return 'Error: division by zero'
        else:
            return divide(a, b)
    else:
        return 'unknown operator'


run = True

while run:

    while True:
        try:
            n1 = float(input('first number: '))
            break
        except ValueError:
            print('Error: please enter valid number')

    while True:
        try:
            n2 = float(input('second number: '))
            break
        except ValueError:
            print('Error: please enter valid number')

    operator = input('operator (+, -, /, *): ')

    print('Result:',calculator(n1,n2,operator))

    while True:
        again = input('Calculate again? (yes/no): ').lower()

        if again == 'no':
            print('Goodbye!')
            run = False
            break

        elif again == 'yes':
            break

        else:
            print('Please enter yes or no')
