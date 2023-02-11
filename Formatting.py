def corrector(my_str, width, symbol):
    s = (f'{my_str: ^{width}}')
    start_str = s[:s.find(my_str[0])]
    end_str = s[s.rfind(my_str[-1])+1:]
    return start_str.replace(" ", symbol) + my_str + end_str.replace(" ", symbol)

my_str = ('Where is the "Hello World!", when it is so needed!?')
width = int(input('Input length symbol '))
symbol = input('Input symbol ')
if width > len(my_str):
    print(corrector(my_str, width, symbol))










