def decorator(func):
        func()
        try:
            print(' ')
            print('The calculator has such mathematical operations:')
            print('--------------------')
            print('Addition = +')
            print('Subtraction = -')
            print('Multiplication = *')
            print('Division = /')
            print('Exponentiation = **')
            print('Rounding = //')
            print('--------------------')
            a = int(input('Enter First Value: '))
            sign = input('Sign: ')
            b = int(input('Enter Second Value: '))
            if sign == '/' and b == 0:
                raise ZeroDivisionError
            if sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != '**' and sign != '//':
                raise Warning
            elif sign == '+':
                print(''), print(f"Result Action: {a} + {b} = {a+b}")
            elif sign == '*':
                print(''), print(f"Result Action: {a} * {b} = {a*b}")
            elif sign == '-':
                print(''), print(f"Result Action: {a} - {b} = {a-b}")
            elif sign == '/':
                print(''), print(f"Result Action: {a} : {b} = {a/b}")
            elif sign == '**':
                print(''), print(f"Result Action: {a} ** {b} = {a**b}")
            elif sign == '//':
                print(''), print(f"Result Action: {a} // {b} = {a//b}")

        except ValueError:
            print('You need to input digits!')

        except ZeroDivisionError:
            print('Division by zero is not possible!')

        except Warning:
            print('Unknown sign!')
@decorator

def deco_1():
    print('The Mathematical Calculator')
    print('---------------------------')
    s_0 = str(input('What is your name:')).isalpha()
    o_0 = str(input('How old are you:')).isnumeric()
    n_0 = str(input('What is your favorite number:')).isnumeric()
    
    n_1 = str(input(n_0))
    s_1 = str(input(s_0))
    o_1 = str(input(o_0))

