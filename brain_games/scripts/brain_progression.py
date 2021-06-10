#!/usr/bin/env python
from brain_games.scripts.cli import welcome_user
import random
import prompt


def make_progression():
    start_pos = random.randint(0, 10)
    num_progress = random.randint(0, 10)
    my_progression = []
    for _ in range(0, 10):
        new_pos = start_pos + num_progress
        my_progression.append(new_pos)
        start_pos = new_pos
    return my_progression


def delete_and_answer(user):
    user_name = user
    arithmetic_progress = make_progression()
    i = random.choice(arithmetic_progress)
    index_hidden = arithmetic_progress.index(i)
    right_answer = arithmetic_progress[index_hidden]
    arithmetic_progress[index_hidden] = '..'
    print('Question: ', end='')
    for x in arithmetic_progress:
        print(x, end=' ')
    print()
    answer = prompt.integer('Your answer: ')
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print('{0} is wrong answer ;(. '
              'Correct answer was {1}.'.format(answer, right_answer))
        print("Let's try again, {0}!".format(user_name))
        return False


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    print('Hello, {}'.format(user))
    right_answers = 0
    print('What number is missing in the progression?')
    while right_answers < 3:
        pass
        if delete_and_answer(user):
            right_answers += 1

    print('Congratulations, {}!'.format(user))


if __name__ == '__main__':
    main()
