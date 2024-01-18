import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(bg="white", padx=20, pady=20)
window.title("Password Manager")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png", width=200, height=200)
canvas.create_image(100,100, image=logo)
# canvas.grid(row=0, column=0)
canvas.pack()

window.mainloop()