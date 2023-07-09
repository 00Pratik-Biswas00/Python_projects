import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):    # Generates next question
        current_question = self.question_list[random.randint(0, len(self.question_list) - 1)]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)? -> ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):    # Checks the result 
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\nYou're right!!")
        else:
            print("\nYou're wrong.")
        print(f"The correct answer is: {correct_answer}\nYour score is: {self.score}/{self.question_number}\n")
