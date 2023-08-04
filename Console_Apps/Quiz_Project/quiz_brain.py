class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect!")
        print(f"The answer is: {actual_answer}")
        print(f"Current score is: {self.score}/{len(self.question_list)}")
        print("")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {current_question.text} (True / False): ")
        self.check_answer(answer, current_question.answer)
