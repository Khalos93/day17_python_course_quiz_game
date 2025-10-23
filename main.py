from data import question_data
from question_model import Question
from quiz_brain import QuizEngine
from util import get_valid_input, valid_play_input

questions_bank = []

for data in question_data:
    question = Question(data['text'], data['answer'])
    questions_bank.append(question)

quiz_engine = QuizEngine(questions_bank)
while True:
    quiz_engine.question_number = 0
    play_game = get_valid_input("Welcome to this trivia game! "
                                "Your goal is figuring out given a question if it is True or False!\n"
                                "Here goes the first question, Are you ready to play? Type Y or N", valid_play_input)

    if play_game == 'n':
        break

    while True:
        response = quiz_engine.next_question()
        if quiz_engine.is_answer_correct(response):
            is_next_question_available = quiz_engine.increase_question_number()
            if is_next_question_available:
                continue
            else:
                break
        else:
            print("You are wrong.")
            print(f"Your final score is {quiz_engine.score}")
            break
