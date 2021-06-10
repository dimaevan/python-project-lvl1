#!/usr/bin/env python
from brain_games.scripts.cli import welcome_user
import random
import prompt


def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    else:
        return 'yes'


def rand_numb(user_name):
    x = random.randint(1, 100)
    print('Question: {0}'.format(x))
    answer = prompt.string('Your answer: ')
    if answer == is_simple(x):
        print('Correct')
        return True
    else:
        print('{0} is wrong answer ;(. '
              'Correct answer was {1}.'.format(answer, is_simple(x)))
        print("Let's try again, {0}!".format(user_name))
        return False


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    print('Hello, {}'.format(user))
    right_answers = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while right_answers < 3:
        pass
        if rand_numb(user):
            right_answers += 1
    print('Congratulations, {}!'.format(user))


if __name__ == '__main__':
    main()
