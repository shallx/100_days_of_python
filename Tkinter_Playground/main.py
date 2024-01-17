import tkinter as tk

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="My label", font=("Ariel", 24, "bold"))
my_label.pack()

# Button
def buttonClick():
    my_label["text"] = input.get()
    

my_button = tk.Button(text="Click me", command=buttonClick)
my_button.pack()

# Entry
input = tk.Entry(width=14)
input.pack()
window.mainloop()