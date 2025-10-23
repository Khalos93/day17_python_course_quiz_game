from data import question_data
from question_model import Question
from quiz_brain import QuizEngine

questions_bank = []

for data in question_data:
    question = Question(data['text'], data['answer'])
    questions_bank.append(question)
    quiz_engine = QuizEngine(questions_bank)

while True:
    response = quiz_engine.next_question()
    if quiz_engine.is_answer_correct(response):
        quiz_engine.increase_question_number()
    else:
        print("You are wrong.")
        print(f"Your final score is {quiz_engine.score}")
        break
