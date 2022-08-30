import prompt


# the function finds out if the user's statement is correct
def checking_correct(question, right_answer, user_name):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f'\'{user_answer}\' is wrong answer ;(.'
              f'Correct answer was \'{right_answer}\'.'
              f'\nLet\'s try again, {user_name}!')


def congratulation_user(counter_right_answer, username, round_count=3):
    if counter_right_answer == round_count:
        print(f'Congratulations, {username}!')
