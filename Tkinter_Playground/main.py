import tkinter as tk

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)


def buttonClick():
    my_label["text"] = input.get()
    
# Label
my_label = tk.Label(text="My label", font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)
    
# Button
my_button = tk.Button(text="Click me", command=buttonClick)
my_button.grid(column=1, row=1)

my_button2 = tk.Button(text="Click me 2", command=buttonClick)
my_button2.grid(column=2, row=0)

# Entry
input = tk.Entry(width=14)
input.grid(column=3, row=3)
window.mainloop()