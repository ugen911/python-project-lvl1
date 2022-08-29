from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct
from random import randint



def is_prime_number():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    round_count = 3
    username = welcome_user()
    counter_right_answer = 0
    
    while counter_right_answer < round_count:
       
        
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
    miss_number()


if __name__ == '__main__':
    main()