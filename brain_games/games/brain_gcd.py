#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct
from random import randint
import math


task = 'Find the greatest common divisor of given numbers.'

def gcd(task=task):
    round_count = 3
    username = welcome_user()
    counter_right_answer = 0
    while counter_right_answer < round_count:
        random_number1 = randint(0, 100)
        random_number2 = randint(0, 100)
        question = str(random_number1)+" "+str(random_number2)
        right_answer = str(math.gcd(random_number1, random_number2))
        result = checking_correct(task=task, question=question, 
                                  right_answer=right_answer, 
                                  user_name=username)
        if result:
            counter_right_answer +=1 
        else:
            break
    if counter_right_answer == round_count:
        print(f'Congratulation {username}')

def main():
    gcd()


if __name__ == '__main__':
    main()