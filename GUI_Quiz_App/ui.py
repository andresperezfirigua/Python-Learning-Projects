from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f'Score: {self.quiz.score}', background=THEME_COLOR, foreground='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=('arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, background=THEME_COLOR, command=self.hit_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, background=THEME_COLOR, command=self.hit_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f'Final score: {self.quiz.score} out of {len(self.quiz.question_list)}\n\n'
                     f'Restart the app to take another quiz'
            )
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def hit_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def hit_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, correct_answer):
        if correct_answer:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
