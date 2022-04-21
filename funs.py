from tkinter import *

from random import randint

# import textbox_output


def tasodifiy():
    number = int(textbox_input.get())

    textbox_output.delete(0.0, END)

    for i in range(1, 11):
        t_son = str(randint(1, number) + '\n')


textbox_output.insert(END, t_son)

window = Tk()

window.title(' Tasodifiy son ')
window.geometry("250x250")

window.configure(background='yellow')

input_label = Label(window, text='Son: ', bg="yellow")

input_label.grid(row=0, columnn=0)
output_label = Label(window, text='\nNatija', bg="yellow")

output_label.grid(row=2, column=0)

textbox_input = Entry(window, width=5)
textbox_input.grid(row=1, column=0)

textbox_output = Text(window, height=10, width=6)

textbox_output.grid(row=3, column=0)

kubik_button = Button(window, text="Tasodifiy son", command=tasodifiy)

kubik_button.grid(row=1, column=1)
window.mainloop()