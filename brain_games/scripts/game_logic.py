def checking_correct(user_answer, right_answer, user_name):
    if user_answer == right_answer:
            print('Correct')
            return True
    else:
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}".
        Let's try again, {user_name}''')
    
def counter_game_round(user_name):
    counter_right_answer = 0
    while counter_right_answer < 3:
        if is_right_answer():
            counter_right_answer += 1
        else:
            break
    if counter_right_answer == 3:
        print(f'Congratulation {user_name}')
