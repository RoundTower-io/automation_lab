while True:
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero!')
    except: 
        print('Unknown error!')
    else:
        print('Result is {}'.format(result))
    finally:
        print('Executing finally clause')