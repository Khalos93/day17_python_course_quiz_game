valid_play_input = ['y', 'n']
valid_answer = ['a', 's']


def get_valid_input(sentence: str, valid_options):
    while True:
        user_response = str(input(sentence)).strip().lower()
        if user_response in valid_options:
            return user_response
        else:
            print('invalid input')
