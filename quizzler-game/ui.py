# used libraries
from tkinter import *
from quiz_brain import QuizBrain


# constants
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """Models UI of the quiz"""
    def __init__(self, quiz_brain: QuizBrain):
        # quiz logic
        self.quiz = quiz_brain
        # UI window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # quiz score
        self.score_label = Label(text=f"Score: 0", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # part of screen presenting questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Question Text",
                                                     font=FONT,
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # button stating answer to question is true
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        # button stating answer to question is false
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        # switch questions
        self.get_next_question()
        # keep window open
        self.window.mainloop()

    def get_next_question(self):
        """Shows next question if there is any question left in the question list"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Looks for the feedback when true button is pressed"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Looks for the feedback when false button is pressed"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Colors the screen in green if the answer is right and red if the answer is wrong"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
