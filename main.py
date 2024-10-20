from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for data in question_data:
    q_obj = Question(data["question"], data["correct_answer"])
    question_bank.append(q_obj)

quiz=  QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")