# used library
import html


class QuizBrain:
    """Models the brain of the quiz"""
    def __init__(self, q_list):
        self.current_question = None
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """Checks if there is unanswered questions in the question list (total of 10 questions)"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Returns next question from the question list"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Checks if the answer is correct"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
