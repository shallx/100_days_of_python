import tkinter as tk
from tkinter import messagebox
import pyperclip
from password import PasswordGenerator
import json


def search_password():
    site = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
                data = json.load(file)
                messagebox.showinfo(title=f"Data Found!", message=f"Email:{data[site]["email"]}\nPassword:{data[site]["password"]}")
                
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found!", message="Data file not found!")
    except Exception as e:
        print(e)
        messagebox.showinfo(title="Website not found", message="No such website found in database")
        
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
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(json_data, file, indent=4)
        except json.JSONDecodeError:
            messagebox.showinfo(title="data.json file is corrupted", message="It is either empty, or json file not properly formatted!")
                
        else:
            data.update(json_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
                print(" i am in else")   
        finally:
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
website_entry = tk.Entry(width=21,fg="black", bg="white")
website_entry.grid(row=1, column=1)
email_entry = tk.Entry(width=38,fg="black", bg="white")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21,fg="black", bg="white")
password_entry.grid(row=3, column=1)

# Button
generate_button = tk.Button(text="Generate Password", command=on_generate, highlightthickness=0).grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=on_save, highlightthickness=0).grid(row=4, column=1, columnspan=2)
search_button = tk.Button(text="Search", width=13, command=search_password, highlightthickness=0).grid(row=1, column=2)

window.mainloop()