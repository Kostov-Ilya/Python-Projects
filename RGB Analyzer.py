from tkinter import*

main = Tk()

main.geometry('200x400')

main.title('RGB Analyzer')

# main.iconbitmap(r'C:\Users\Win10_Game_OS\Desktop\Портфолио\Development & Programming\Html\Html Favicons')

def insert_1():
    entry.insert(0, '#FF0000')

def insert_2():
    entry.insert(0, '#FFA500')

def insert_3():
    entry.insert(0, '#FFD700')

def insert_4():
    entry.insert(0, '#008000')

def insert_5():
    entry.insert(0, '#00BFFF')

def insert_6():
    entry.insert(0, '#00008B')

def insert_7():
    entry.insert(0, '#9400D3')

def work_1():
    entry.delete(0, END)
    entry.insert(0, '#FF0000')
def work_2():
    entry.delete(0, END)
    entry.insert(0, '#FFA500')
def work_3():
    entry.delete(0, END)
    entry.insert(0, '#FFD700')
def work_4():
    entry.delete(0, END)
    entry.insert(0, '#008000')
def work_5():
    entry.delete(0, END)
    entry.insert(0, '#00BFFF')
def work_6():
    entry.delete(0, END)
    entry.insert(0, '#00008B')
def work_7():
    entry.delete(0, END)
    entry.insert(0, '#9400D3')


entry = Entry(width=25, justify='center', bd=5,relief='groove')
entry.pack()

b_1= Button(main,bg='#FF0000', width=30, height=3,command=work_1)
b_1.pack()

b_2 = Button(main, bg='#FFA500', width=30, height=3, command=work_2)
b_2.pack()

b_2 = Button(main, bg='#FFD700', width=30, height=3, command=work_3)
b_2.pack()

b_2 = Button(main, bg='#008000', width=30, height=3, command=work_4)
b_2.pack()

b_2 = Button(main, bg='#00BFFF', width=30, height=3, command=work_5)
b_2.pack()

b_2 = Button(main, bg='#00008B', width=30, height=3, command=work_6)
b_2.pack()

b_2 = Button(main, bg='#9400D3', width=30, height=3, command=work_7)
b_2.pack()

mainloop()