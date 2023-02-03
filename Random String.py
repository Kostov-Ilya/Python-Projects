import random

my_str = 'Where is the "Hello World!", when it is so needed!?'
symbol = random.choice('HELLOWORLD!GOODBYEWORLD!')
t = random.randint(0, len(my_str)-1)
new_str_1 = my_str[:t]
new_str_2 = my_str[t:]
print(new_str_1 + symbol + new_str_2)

