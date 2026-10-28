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

