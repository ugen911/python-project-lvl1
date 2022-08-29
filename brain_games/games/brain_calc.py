#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct
from random import randint, choice

def calc():
    username = welcome_user()
    counter_right_answer = 0
    operators = ['+', '-', '*']
    task = 'What is the result of the expression?'
    while counter_right_answer < 3:
        random_number1 = randint(0, 100)
        random_number2 = randint(0, 100)
        random_operator = choice(operators)
        question = str(random_number1)+random_operator+str(random_number2)
        right_answer = str(eval(question))
        result = checking_correct(task=task, question=question, 
                                  right_answer=right_answer, 
                                  user_name=username)
        if result:
            counter_right_answer +=1 
        else:
            break
    if counter_right_answer == 3:
        print(f'Congratulation {username}')


def main():
    calc()


if __name__ == '__main__':
    main()
