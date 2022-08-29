from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import checking_correct
from random import randint


def miss_number():
    task = 'What number is missing in the progression?'
    round_count = 3
    username = welcome_user()
    counter_right_answer = 0

    while counter_right_answer < round_count:
        progression_list = []
        len_progression = randint(5, 11)
        symbol = randint(0, 100)
        step_of_progression = randint(1, 10)

        for i in range(len_progression):
            progression_list.append(symbol)
            symbol += step_of_progression

        element_progression = progression_list[randint(0, len_progression - 1)]
        question = ''

        for i in progression_list:
            if element_progression == i:
                question = question + ' ' + '..'
            else:
                question = question + ' ' + str(i)

        right_answer = str(element_progression)

        result = checking_correct(task=task, question=question,
                                  right_answer=right_answer,
                                  user_name=username)
        if result:
            counter_right_answer += 1
        else:
            break
    if counter_right_answer == round_count:
        print(f'Congratulation {username}')


def main():
    miss_number()


if __name__ == '__main__':
    main()
