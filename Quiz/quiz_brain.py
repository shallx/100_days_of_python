class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def totalQuestions(self):
        return len(self.question_list)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, question):
        ans = user_answer
        while not (ans == "true" or ans == "t" or ans == "false" or ans == "f"):
            print("Invalid input, try again!")
            ans = input(f"Q.{self.question_number} {question.text} (True/False)?: ").lower()
        
        ans = "True" if ans == "true" or ans == "t" else "False"
        
        if ans == question.answer:
            print("You got it right ✅")
            self.score += 1
        else:
            print("That's wrong ❌")
            print(f"Correct answer is {question.answer}")
        
        print(f"Your current score is {self.score}/{self.question_number}\n")
        

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number} {question.text} (True/False)?: ").lower()
        self.check_answer(ans, question)