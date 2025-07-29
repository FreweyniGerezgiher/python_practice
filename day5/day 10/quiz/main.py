from question_model import Question
from data import Qdata
from quiz_brain import QuizBrain
question_bank = []
for question in Qdata:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz")
print(f"your final score was{quiz.score}/{quiz.q_number}")