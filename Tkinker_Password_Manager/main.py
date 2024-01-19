import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(bg="white", padx=20, pady=20)
window.title("Password Manager")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=0)

# Label
website_label = tk.Label(text="Website:",fg="black", bg="white").grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:",fg="black", bg="white").grid(row=2, column=0)
password_label = tk.Label(text="Password:",fg="black", bg="white").grid(row=3, column=0)


# Entry
website_entry = tk.Entry(width=35,fg="black", bg="white").grid(row=1, column=1, columnspan=2)
email_entry = tk.Entry(width=35,fg="black", bg="white").grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21,fg="black", bg="white").grid(row=3, column=1)

# Button
generate_button = tk.Button(text="Generate Password").grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36).grid(row=4, column=1, columnspan=2)

window.mainloop()