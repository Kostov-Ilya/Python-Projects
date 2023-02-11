import datetime

while True:
    select = input('Yes i want to enter! / No i want to enter!:')
    if select.capitalize() == "Yes":
        s = input('Enter Your Years,Month,Day:')
        new_date = datetime.datetime.now()
        s = new_date.strptime(s, '%Y %m %d')
        date = new_date.strftime('%Y : %m : %d')
        with open('text.txt', 'w') as s:
            s.write(f'{date}')
    else:
        break

