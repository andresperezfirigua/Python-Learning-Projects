# Lesson Challenge

# tkinter app that displays random quote provided from a free API, using the GET http method

# import requests
# from tkinter import *
#
#
# def get_quote():
#     response = requests.get(url='https://api.quotable.io/quotes/random?maxLength=87&tags=education|inspirational'
#                                 '|knowledge|mathematics|motivational|perseverance|science|technology|work')
#     response.raise_for_status()
#
#     data = response.json()
#     quote = data[0]['content']
#     author = data[0]['author']
#
#     canvas.itemconfig(quote_text, text=f'{quote} - {author}')
#
#
# window = Tk()
# window.title("Quoty")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, width=250, font=("Arial", 25, "bold"),
#                                 fill="white")
# canvas.grid(row=0, column=0)
#
# next_img = PhotoImage(file="swipe.png")
# next_button = Button(image=next_img, highlightthickness=0, command=get_quote, width=80, height=80, background='black')
# next_button.grid(row=1, column=0)
#
# get_quote()
# window.mainloop()
