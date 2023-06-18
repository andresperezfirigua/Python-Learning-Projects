# import tkinter
#
# window = tkinter.Tk()
# window.title('GUI')
#
# window.mainloop()

# Passing multiple positional arguments to a function or method, this will create a
# tuple with the values of the passed arguments
# def add(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result
#
#
# num_sum = add(1,3,4,5,6,7,8)
#
# print(num_sum)


# Passing multiple keyword arguments to a function or a method, this will create a
# dictionary with the key value pairs of the arguments that we passed

# def calculate(**kwargs):
#     result = 10
#     result += kwargs["sum"]
#     result *= kwargs["multiply"]
#     print(result)
#
#
# calculate(sum=2, multiply=4)


# Below are the most basic controls in TKinter
# from tkinter import *
#
# window = Tk()
# window.title('GUI')
# window.minsize(width=500, height=300)
# label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# label.pack()
#
#
# def button_clicked():
#     print("I got clicked")
#     label.config(text=inputText.get())
#
#
# button = Button(text="Click me", command=button_clicked)
# button.pack()
#
# inputText = Entry()
# inputText.pack()
#
#
# window.mainloop()

# Here are more advanced controls in TKinter

#Creating a new window and configurations

# from tkinter import *
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


# Here are the 3 methods that allow positioning of the controls across the window,
# pack(), place(), grid() (This last one is the most recommended)

# In addition to the above methods for positioning,
# there is a property in the config() method called pad to add space between controls so they don't crash together

# from tkinter import *
#
# window = Tk()
# window.title('GUI')
# window.minsize(width=500, height=300)
# label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# # label.pack()
# # label.place(x=0, y=0)
# label.grid(column=0, row=0)
#
#
# def button_clicked():
#     print("I got clicked")
#     label.config(text=inputText.get())
#
#
# button = Button(text="Click me", command=button_clicked)
# # button.pack()
# # button.place(x=50, y=20)
# button.grid(column=1, row=1)
#
# button2 = Button(text="New button", command=button_clicked)
# # button.pack()
# # button2.place(x=100, y=40)
# button2.grid(column=3, row=0)
#
# inputText = Entry()
# # inputText.pack()
# # inputText.place(x=150, y=80)
# inputText.grid(column=4, row=3)
#
# window.mainloop()
