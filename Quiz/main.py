from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from trivia import question_data

# question_data = [Question(question["text"], question["answer"]) for question in question_data]
question_data = [Question(question["question"], question["correct_answer"]) for question in question_data]

quizBrain = QuizBrain(question_data)



while quizBrain.still_has_questions():
    quizBrain.next_question()

print(f"Your final score is {quizBrain.score}/{quizBrain.totalQuestions()}")