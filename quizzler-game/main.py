# used libraries
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# list of questions
question_bank = []

# fill the list with questions
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create objects that run the quiz
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
