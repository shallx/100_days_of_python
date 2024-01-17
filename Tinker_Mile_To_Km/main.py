import tkinter as tk

def convert():
    miles = int(miles_input.get())
    to_km = round(miles * 1.61, 2)
    to_km_label.config(text=to_km)

window = tk.Tk()
window.minsize(width=200, height=140)
window.title("Mile to Km Converter")
window.config(padx=16, pady=16)

my_label = tk.Label(text="is equal to")
my_label.grid(row=1, column=0)

miles_input = tk.Entry()
miles_input.grid(row=0, column=1)

to_km_label = tk.Label(text="")
to_km_label.grid(row=1, column=1)

calculate_button = tk.Button(text="Calculate", command=convert)
calculate_button.grid(row=2, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = tk.Label(text="km")
km_label.grid(row=1, column=2)

window.mainloop()

