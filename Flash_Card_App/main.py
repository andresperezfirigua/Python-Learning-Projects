import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TO_LEARN_FILE = 'data/words_to_learn.csv'
STARTING_FILE = 'data/Italian_word_list.csv'

current_word = {}
data = None

# Read CSV and get a list
try:
    data = pandas.read_csv(TO_LEARN_FILE)
except FileNotFoundError:
    data = pandas.read_csv(STARTING_FILE)

word_list = data.to_dict(orient='records')

# |-------------- Update list -------------------|


def update_list():
    word_list.remove(current_word)
    temp_data = pandas.DataFrame(word_list)
    temp_data.to_csv(TO_LEARN_FILE, index=False)
    get_next_card()

# |--------------- Pick word --------------------|


def get_next_card():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(word_list)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(language_text, text='Italian', fill='black')
    canvas.itemconfig(word_text, text=current_word['Italian'], fill='black')
    timer = window.after(3000, flip_card)


# |------------------ Flip the card -----------------------|


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, text='Spanish', fill='white')
    canvas.itemconfig(word_text, text=current_word['Spanish'], fill='white')


# |------------------- Create GUI -------------------------|
window = Tk()
window.title("Flash Card App")
timer = window.after(3000, flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

yes_image = PhotoImage(file='images/right.png')
yes_button = Button(image=yes_image, highlightthickness=0, command=update_list)
yes_button.grid(column=1, row=1)

no_image = PhotoImage(file='images/wrong.png')
no_button = Button(image=no_image, highlightthickness=0, command=get_next_card)
no_button.grid(column=0, row=1)

get_next_card()

window.mainloop()
