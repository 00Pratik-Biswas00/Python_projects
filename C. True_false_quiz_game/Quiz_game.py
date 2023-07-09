from data import question_data    # importing other created files
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)		# Generating new questions
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


def play_game():
    while quiz.question_number < 10:	# Run up to a set of 10 questions
        quiz.next_question()
    print("You've completed the quiz!\nYour final score is: {quiz.score}/{quiz.question_number}")
    quiz.question_number = 0	# Assign the value 0 to replay the game and to calculate the score from the starting
    quiz.score=0

while input("\nDo you like to play a quiz game? There will be 10 questions in a set. Tap 'y' for yes and any other key for no->  ") == 'y':	# Taking multiple inputs
    play_game()
