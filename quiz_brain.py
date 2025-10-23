from util import get_valid_input, valid_answer


class QuizEngine:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        print(self.question_list[self.question_number].text)
        answer = get_valid_input("Type 'a' for True and 's' for False", valid_answer)
        if answer == 'a':
            answer = "True"
        else:
            answer = 'False'

        return answer

    def is_answer_correct(self, response: str):
        if response == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"Your score is: {self.score}")
            return True
        else:
            print(f'Your final score is {self.score}')
            return False

    def increase_question_number(self):
        if self.question_number < len(self.question_list) - 1:
            self.question_number += 1
            return True
        else:
            print('You guessed successfully all the questions!\nCongratulation! You terminate the game!')
            return False


