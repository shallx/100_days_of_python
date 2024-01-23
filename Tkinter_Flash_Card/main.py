import tkinter as tk
from card_manager import Card_Manager

# Constants
BACKGROUND_COLOR = "#B1DDC6"
JAP_FONT = ("Ariel", 40, "italic")
ENG_FONT = ("Ariel", 60, "bold")
FLIP_TIME = 3000


# Variables
lang = {}
    

# Counter
def flip_card():
    '''Flips card to show english word by changing background'''
    global lang
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=lang[0], fill="white")

def next_language():
    global lang, flip_timer
    window.after_cancel(flip_timer)
    lang = card_manager.pickOne()
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, text="Japanese", fill="black")
    canvas.itemconfig(word_text, text=lang[1], fill="black")
    flip_timer = window.after(FLIP_TIME, flip_card)

window = tk.Tk()
window.config(width=800, height=526, padx=50, pady=50, bg=BACKGROUND_COLOR)

right_img = tk.PhotoImage(file="./images/right.png")
wrong_img = tk.PhotoImage(file="./images/wrong.png")
card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")
right_button = tk.Button(image=right_img, highlightthickness=0, border=0, command=next_language)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, border=0, command=next_language)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400,150, text="Japanese", fill="black", font=JAP_FONT)
word_text = canvas.create_text(400,263, text="English", fill="black", font=ENG_FONT)
canvas.pack()

# Grids
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

card_manager = Card_Manager()
# card_manager.print()
lang = card_manager.pickOne()
canvas.itemconfig(title_text, text="Japanese")
canvas.itemconfig(word_text, text=lang[1])

flip_timer = window.after(FLIP_TIME, flip_card)
next_language()
window.mainloop()