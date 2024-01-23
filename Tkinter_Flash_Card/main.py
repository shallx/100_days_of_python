import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
JAP_FONT = ("Ariel", 40, "italic")
ENG_FONT = ("Ariel", 60, "bold")

window = tk.Tk()
window.config(width=800, height=526, padx=50, pady=50, bg=BACKGROUND_COLOR)

right_img = tk.PhotoImage(file="./images/right.png")
wrong_img = tk.PhotoImage(file="./images/wrong.png")
card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")
right_button = tk.Button(image=right_img, highlightthickness=0, border=0)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, border=0)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400,150, text="Japanese", fill="black", font=JAP_FONT)
canvas.create_text(400,263, text="English", fill="black", font=ENG_FONT)
canvas.pack()

# Grids
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)


window.mainloop()