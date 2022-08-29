#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct
from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_number(task):
    username = welcome_user()
    counter_right_answer = 0
    while counter_right_answer < 3:
        right_answer = 'no'
        random_number = randint(0, 100)
        question = str(random_number)
        if random_number % 2 == 0:
            right_answer = 'yes'
        result = checking_correct(task=task, question=question, 
                                   right_answer=right_answer, 
                                   user_name=username)
        if result:
            counter_right_answer += 1
        else:
            break
    if counter_right_answer == 3:
        print(f'Congratulation {username}')


def main():
    even_number(task=task)


if __name__ == '__main__':
    main()
