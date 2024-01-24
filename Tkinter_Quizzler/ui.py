from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    timer = None

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_entry = Label(text=f"Score {0}", bg=THEME_COLOR, fg="white")
        self.score_entry.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="Some question are here", fill=THEME_COLOR, font=("Ariel", 16, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=lambda: self.check_question("true"))
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: self.check_question("false"))
        self.wrong_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()
        
    def next_question(self):
        self.question_canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"Quiz challenge completed, you scored {self.quiz.score}/{len(self.quiz.question_list)}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        
        
    def check_question(self, ans):
        self.give_feedback_and_next(self.quiz.check_answer(ans))
        self.update_score(self.quiz.score)
        
        
    def update_score(self, score):
        self.score_entry.config(text=f"Score {score}")
        
    def give_feedback_and_next(self, is_right):
        try:
            self.window.after_cancel(self.timer)
        except:
            pass
        finally:
            self.question_canvas.config(bg="green" if is_right else "red")
            self.timer = self.window.after(1000,func=self.next_question)
        
