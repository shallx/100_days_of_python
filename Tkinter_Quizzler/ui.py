from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_entry = Label(text=f"Score {0}", bg=THEME_COLOR, fg="white")
        self.score_entry.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_canvas.create_text(150, 125, text="Some question are here", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
