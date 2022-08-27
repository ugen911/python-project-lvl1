#!/usr/bin/env python3

from random import randint
import prompt

def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello {username}!')
    return username

def even_number():
    username = welcome_user()
    counter_right_answer = 0
    
    def is_right_answer():
        right_answer = ''
        print('Answer "yes" if the number is even, otherwise answer "no".')
        random_number = randint(0,100)
        print(f'Question:{random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if answer == right_answer:
            print('Correct')
            return True
        else:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".
            Let's try again, {username}''')

    
    while counter_right_answer < 3:
        if is_right_answer():
            counter_right_answer += 1
        else:
            break
    if counter_right_answer == 3:
        print (f'Congratulation {username}')    
        
    



def main():
    even_number()


if __name__ == '__main__':
    main()