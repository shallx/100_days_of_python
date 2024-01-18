import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = 1.3
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
    elif reps % 2 == 0:
        count_down(short_break)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count = int(count)
    count_min = count//60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # for some reason, i can use tk.PhotoImage directly here, needed variable declaration
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", bg=GREEN, highlightthickness=0, bd=0, padx=0, pady=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", bg=GREEN, highlightthickness=0, bd=0, command=None, padx=0, pady=0)
reset_button.grid(row=2, column=2)

check_label = tk.Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_label.grid(row=3, column=1)




window.mainloop()