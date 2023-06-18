from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)

km_value = 0

inputText = Entry(width=7)
inputText.focus()
inputText.insert(0, f'0')
inputText.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.config(padx=10)
label2.grid(column=0, row=1)

labelOutput = Label(text='0', width=10)
labelOutput.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)


def convert():
    mile_value = float(inputText.get())
    result = round(mile_value * 1.609344, 2)
    labelOutput.config(text=result)


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)
window.mainloop()
