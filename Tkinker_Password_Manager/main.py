import tkinter as tk
from tkinter import messagebox
import pyperclip
from password import PasswordGenerator
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def on_generate():
    password_entry.delete(0, tk.END)
    password = PasswordGenerator().generate()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    json_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please fill up all fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered. \nEmail:{email} \nPassword:{password} \nIs it ok to save?")

        if is_ok:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                print(data)
                # data.update(json_data)
                # json.dump(json_data, file, indent=4)

        website_entry.delete(0,tk.END)
        email_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)

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
website_entry = tk.Entry(width=35,fg="black", bg="white")
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tk.Entry(width=35,fg="black", bg="white")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21,fg="black", bg="white")
password_entry.grid(row=3, column=1)

# Button
generate_button = tk.Button(text="Generate Password", command=on_generate).grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=on_save).grid(row=4, column=1, columnspan=2)

window.mainloop()