#!/usr/bin/env python3

from brain_games.scripts.brain_games import main
from random import randint
import prompt



def even_number():
    counter_right_answer = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    def is_right_answer():
        random_number = randint(0,100)
        print(f'Question:{random_number}')
        answer = prompt.string('Your answer: ')  
        if random_number // 2 == 0 and answer == 'yes' or random_number // 2 == 1 and answer == 'no':
            return True
        return answer
    
    while counter_right_answer < 3:
        if is_right_answer() == True:
            print('Correct')
            counter_right_answer += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'./nLet's try again, Bill!")
            break
    print("Congratulations, Bill!")

    even_number()






if __name__ == '__main__':
    main()
