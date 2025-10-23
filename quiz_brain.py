class QuizEngine:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        print(self.question_list[self.question_number].text)
        answer = input(f"Type 'a' for True and 's' for False")
        if answer == 'a':
            answer = "True"
        else:
            answer = 'False'

        return answer

    def is_answer_correct(self, response: str):
        if response == self.question_list[self.question_number].answer:
            self.score += 1
            return True
        else:
            return False

    def increase_question_number(self):
        self.question_number += 1
        print(f"Your score is: {self.score}")
