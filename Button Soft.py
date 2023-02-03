from tkinter import *

def click_1():
    Image_1 = PhotoImage(file=r'C:\Users\Win10_Game_OS\Downloads\Image\Duck_1.gif')
    label_1 = Label(image=Image_1)
    label_1.pack()

def click_2():

    Image_2 = PhotoImage(file=r'C:\Users\Win10_Game_OS\Downloads\Image\Duck_2.gif')
    label_2 = Label(image=Image_2)
    label_2.pack()

def click_3():

    Image_3 = PhotoImage(file=r'C:\Users\Win10_Game_OS\Downloads\Image\Duck_3.gif')
    label_3 = Label(image=Image_3)
    label_3.pack()

def click_4():

    Image_4 = PhotoImage(file=r'C:\Users\Win10_Game_OS\Downloads\Image\Duck_4.gif')
    label_4 = Label(image=Image_4)
    label_4.pack()

def clear():
    main.grid()
    button_1.grid()
    button_2.grid()
    button_3.grid()
    button_4.grid()
    button_5.grid()


main = Tk()

main.geometry('300x250')

main.iconbitmap(r'C:\Users\Win10_Game_OS\Downloads\Image\bomb.ico')

main.title('Button Types')

main.resizable(False, True)

main.minsize(width=100, height=200)

main.maxsize(width=400, height=300)

button_1 = Button(main,text='View Images', font=('Agency FB', 15, 'bold'),
fg = 'white', bg = 'green', width = 15, command = click_1)

button_1.pack()

button_2 = Button(main,text='View Images', font=('Agency FB', 15, 'bold'),
fg = 'white', bg = 'blue',width = 15,command = click_2)

button_2.pack()

button_3 = Button(main,text='View Images', font=('Agency FB', 15, 'bold'),
fg = 'white', bg = 'yellow',width = 15,command = click_3)

button_3.pack()

button_4 = Button(main,text='View Images', font=('Agency FB', 15, 'bold'),
fg = 'white', bg = 'grey',width = 15,command = click_4)

button_4.pack()

button_5 =  Button(main,text='Clear Soft', font=('Agency FB', 15, 'bold'),
fg = 'white', bg = 'red',width = 15,command = clear)

button_5.pack()

mainloop()