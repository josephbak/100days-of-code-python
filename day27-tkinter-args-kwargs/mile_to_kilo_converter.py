from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)


#Label
label1 = Label(text = "Miles", font = ("Arial", 24, "normal"))
# my_label.pack()
# my_label.config(text = "New Text")
# my_label.place(x=100, y=200)
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)
# my_label["text"] = "New Text"

label2 = Label(text = "is equal to", font = ("Arial", 24, "normal"))
label2.grid(column=0, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text = "0")
label3.grid(column= 1, row = 1)
label3.config(padx=20, pady=10)


label4 = Label(text = "Km", font = ("Arial", 24, "normal"))
label4.grid(column= 2, row = 1)
label4.config(padx=10, pady=10)


#Entry
input = Entry(width = 10)
input.grid(column= 1, row = 0)


#Button
def button_clicked():
    miles = float(input.get())
    kilos = round(1.609*miles)
    label3.config(text=str(kilos))

button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row=2)



window.mainloop()



