from functools import partial
from tabnanny import check
from tkinter import *
from quiz_brain import QuizBrain

class QuizzlerInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.THEME_COLOR = "#375362"
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=self.THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=400, height=350)
        self.question_text = self.canvas.create_text(200,175,width=380,text="Question goes here...", font=("Arial", 18, "italic"))

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, padx=20, pady=20, cursor="hand2", command=lambda: self.check_answer("True"))
        self.false_button = Button(image=false_image, padx=20, pady=20, cursor="hand2",command=lambda: self.check_answer("False"))
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), fg="WHITE", bg=self.THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=3, padx=20, pady=30)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=2)
        self.score_label.grid(row=0, column=2)

        self.get_question()

        self.window.mainloop()


    def get_question(self):
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except Exception as e:
            print(f"Error: {e}")

    def check_answer(self, ans: str):
        print(ans)
        self.quiz.check_answer(ans)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_question()






