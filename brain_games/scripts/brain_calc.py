#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct, congratulation_user
from random import randint, choice


def calc():
    operators = ['+', '-', '*']
    task = 'What is the result of the expression?'
    round_count = 3
    username = welcome_user()
    print(task)
    counter_right_answer = 0
    while counter_right_answer < round_count:
        random_number1 = randint(0, 100)
        random_number2 = randint(0, 100)
        random_operator = choice(operators)
        question = str(random_number1) + random_operator + str(random_number2)
        right_answer = str(eval(question))
        result = checking_correct(question=question,
                                  right_answer=right_answer,
                                  user_name=username)
        if result:
            counter_right_answer += 1
        else:
            break

    congratulation_user(counter_right_answer, username)


def main():
    calc()


if __name__ == '__main__':
    main()
