import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(width=800, height=526, padx=50, pady=50)

right_img = tk.PhotoImage(file="/images/right.png")
wrong_img = tk.PhotoImage(file="/images/wrong.png")
card_front = tk.PhotoImage(file="/images/card_front.png")
card_back = tk.PhotoImage(file="/images/card_back.png")
button = tk.Button(image=right_img, highlightthickness=0)
button = tk.Button(image=wrong_img, highlightthickness=0)