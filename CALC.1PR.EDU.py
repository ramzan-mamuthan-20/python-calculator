run=True
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
    operator=input('operator(+,-,/,*): ')

    if operator =='+':
        print('result',n1+n2)
    elif operator =='-':
        print('result',n1-n2)
    elif operator =='/':
        if n2==0:
            print('err')
        else:
            print('result',n1/n2)
    elif operator=='*':
        print('result',n1*n2)
    else:
        print('unknown operator')
    while True:
        again=input('Calculate again?(yes/no): ').lower()
        if again== 'no':
            print('Goodbye!')
            run=False
            break
        elif again=='yes':
            break
        else:
            print('Please enter yes or no')

