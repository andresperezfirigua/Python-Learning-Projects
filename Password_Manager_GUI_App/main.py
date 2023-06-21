import tkinter
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

FONT_NAME = "Arial"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters, nr_symbols, nr_numbers = 0, 0, 0
    length = random.randint(12, 15)

    while nr_letters + nr_symbols + nr_numbers != length:
        nr_letters = random.randint(4, length)
        nr_symbols = random.randint(4, length)
        nr_numbers = random.randint(4, length)

    letters = [LETTERS[random.randint(0, len(LETTERS) - 1)] for _ in range(0, nr_letters)]
    symbols = [SYMBOLS[random.randint(0, len(SYMBOLS) - 1)] for _ in range(0, nr_symbols)]
    numbers = [NUMBERS[random.randint(0, len(NUMBERS) - 1)] for _ in range(0, nr_numbers)]

    password = letters + symbols + numbers

    random.shuffle(password)

    printable_password = "".join(password)

    password_text.delete(0, END)
    password_text.insert(0, printable_password)

    # Automatically copying the current generated password to the clipboard for it to be pasted somewhere else
    pyperclip.copy(printable_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = website_text.get().strip()
    username = user_text.get().strip()
    password = password_text.get().strip()

    length_website = len(website)
    length_user = len(username)
    length_password = len(password)

    if length_website and length_user and length_password != 0:
        is_confirmed = messagebox.askokcancel(title=website_text.get(), message=f'This is the information entered:\n'
                                                                                f'Email: {username}\n'
                                                                                f'Password: {password}\n'
                                                                                f'Is it ok to save?')
        if is_confirmed:
            with open('./data.txt', mode='a') as file:
                file.write(f'{website} | {username} | {password}\n')
            website_text.delete(0, END)
            password_text.delete(0, END)
    else:
        messagebox.showerror(title='Missing information', message='Please, do not leave any field empty')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text='Website:', font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)

website_text = Entry(width=57)
website_text.grid(column=1, row=1, columnspan=2, sticky=tkinter.W)
website_text.focus()

user_label = Label(text='Email/Username:', font=(FONT_NAME, 10))
user_label.grid(column=0, row=2)

user_text = Entry(width=57)
user_text.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)
user_text.insert(0, "andrespf@outlook.com")

password_label = Label(text='Password:', font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

# TODO Add property: show='*' will cover my password, pending improvement adding show/hide button
password_text = Entry(width=34)
password_text.grid(column=1, row=3, sticky=tkinter.W)

generate_pw_button = Button(text='Generate Password', font=(FONT_NAME, 10, 'bold'), bg='#de6c5b', fg='white', command=generate_password)
generate_pw_button.grid(column=2, row=3, sticky=tkinter.W)

add_button = Button(text='Add', font=(FONT_NAME, 10, 'bold'), width=42, bg='#de0000', fg='white', command=add_entry)
add_button.grid(column=1, row=4, columnspan=2, sticky=tkinter.W)

window.mainloop()
