#import the 'tkinter module
from tkinter import*
root = Tk()


root.title("Adding two numbers")


label1 = Label(root, text = "Please enter first number:");
label2 = Label (root, text = "Please enter second number:")
label3 = Label(root, text="Your answer:")
label4=Label(root)

first_num = Entry (root )
second_num = Entry(root)
answer = Entry(root)

def button_clear ():

    answer.delete(0, END)
    first_num.delete(0,END)
    second_num.delete(0,END)

def button_add ():
    digit_1 = first_num.get();
    digit_2 = second_num.get();
    first_add = int(digit_1)
    second_add = int (digit_2)
    answer.insert(0, first_add + second_add)

def button_exit ():
    import sys
    sys.exit()

button_add = Button(root,borderwidth=10,text="Add", width=15, command=button_add)
button_clear = Button(root, text="Clear", borderwidth=10, width=15, command=button_clear)
button_exit = Button(root, text="Exit", borderwidth=10, width=15, command=button_exit)


label1.grid(row=0, column=0, padx=10, pady=10 )
label2.grid(row=1,column=0, padx=10, pady=10)
label3.grid(row=2,column=0, padx=10, pady=10)
first_num.grid(row=0,column=1, padx=10, pady=10)
second_num.grid(row=1,column=1, padx=10, pady=10)
answer.grid(row=2,column=1, padx=10, pady=10)
button_add.place(x=20, y=150)
button_clear.place(x=200, y=150)
button_exit.place(x=380, y=150)

root.mainloop()
