import prompt


def checking_correct(task, question, right_answer, user_name):
    print(task)
    print(question)
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
            print('Correct')
            return True
    else:
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}".
        Let's try again, {user_name}''')
    






# def is_right_answer():
#         right_answer = ''
#         print('Answer "yes" if the number is even, otherwise answer "no".')
#         random_number = randint(0, 100)
#         print(f'Question:{random_number}')
#         answer = prompt.string('Your answer: ')
#         if random_number % 2 == 0:
#             right_answer = 'yes'
#         else:
#             right_answer = 'no'
#         if answer == right_answer:
#             print('Correct')
#             return True
#         else:
#             print(f'''"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".
#             Let's try again, {username}''')