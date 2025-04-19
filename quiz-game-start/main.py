from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    Q_text = question['question']
    Ans = question['correct_answer']
    question = Question(Q_text, Ans)
    question_bank.append(question)

quiz_brain = Quizbrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You have completed the quiz.")
print(f"Your final score is:{quiz_brain.score}/{quiz_brain.question_number}")
