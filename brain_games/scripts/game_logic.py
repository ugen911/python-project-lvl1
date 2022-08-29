import prompt


# the function finds out if the user's statement is correct
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
